from unittest.mock import PropertyMock

import asyncio
import pytest
import json

from galaxy.api.types import Game, LicenseInfo
from galaxy.api.consts import LicenseType

from definitions import Blizzard
from tests.website_mocks import backend_owned_games, backend_classic_games


@pytest.fixture
def result_owned_games():
    vals = [
        Blizzard['wow'],
        Blizzard['odin'],
        Blizzard['s1'],
        Blizzard['s2'],
        Blizzard['prometheus'],
        Blizzard['diablo3'],
        Blizzard['hs_beta'],
        Blizzard['heroes'],
        Blizzard['wow_classic']
    ]

    return [
        Game(game.uid, game.name, None, LicenseInfo(LicenseType.SinglePurchase))
        for game in vals
    ]


@pytest.fixture
def result_classic_games():
    return [
        Game('d2', 'Diablo® II', None, LicenseInfo(LicenseType.SinglePurchase)),
    ]


@pytest.mark.asyncio
async def test_owned_games(pg, backend_mock, backend_owned_games, result_owned_games):
    backend_mock.get_owned_games.return_value = backend_owned_games
    backend_mock.get_owned_classic_games.return_value = {'classicGames': []}

    result = await pg.get_owned_games()
    assert sorted(result, key=lambda x: x.game_id) == sorted(result_owned_games, key=lambda x: x.game_id)


@pytest.mark.asyncio
@pytest.mark.parametrize('china', [False, True])
async def test_try_for_free_games(china, mocker, pg, backend_mock):
    backend_mock.get_owned_games.return_value = {'gameAccounts': []}
    backend_mock.get_owned_classic_games.return_value = {'classicGames': []}
    mocker.patch('plugin.AuthenticatedHttpClient.region', new_callable=PropertyMock(return_value='cn' if china else 'eu'))

    expected = [
        Game(g.uid, g.name, None, LicenseInfo(LicenseType.FreeToPlay))
        for g in Blizzard.try_for_free_games(cn=china)
    ]
    result = await pg.get_owned_games()
    assert sorted(result, key=lambda x: x.game_id) == sorted(expected, key=lambda x: x.game_id)


@pytest.mark.asyncio
async def test_integration(
    pg, backend_mock, backend_owned_games, backend_classic_games, result_owned_games, result_classic_games
):
    backend_mock.get_owned_games.return_value = backend_owned_games
    backend_mock.get_owned_classic_games.return_value = backend_classic_games

    result = await pg.get_owned_games()
    assert sorted(result, key=lambda x: x.game_id) == sorted(result_owned_games + result_classic_games, key=lambda x: x.game_id)

