import pytest

from playlist_logic import search_songs, random_choice_or_none


SONG1 = {"title": "Levitating", "artist": "Dua Lipa", "genre": "pop", "energy": 8, "tags": ["dance"]}
SONG2 = {"title": "Bohemian Rhapsody", "artist": "Queen", "genre": "rock", "energy": 8, "tags": ["classic"]}


def test_search_partial_match():
    songs = [SONG1, SONG2]
    res = search_songs(songs, "dua", field="artist")
    assert len(res) == 1
    assert res[0]["artist"].lower().startswith("dua")


def test_search_empty_query_returns_all():
    songs = [SONG1, SONG2]
    res = search_songs(songs, "", field="artist")
    assert res == songs


def test_random_choice_empty_returns_none():
    assert random_choice_or_none([]) is None


def test_random_choice_single_returns_item():
    item = {"title": "X", "artist": "A", "genre": "g", "energy": 1}
    assert random_choice_or_none([item]) == item
