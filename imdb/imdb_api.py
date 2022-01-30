import requests
import json
from .response import (
    Top250Movies, Top250TVs,
    MostPopularMovies, MostPopularTVs,
    SearchMovies, SearchSeries,
    Title, BoxOffices,
    BoxOfficeAll, ComingSoon,
    SearchKeyword, Keyword,
    InTheaters, Name,
)
from .core import ApiCall


class IMDB:
    """
        PYTHON IMDb API

        Attributes
        ----------
        api_key: str
            IMDB API KEY
    """
    def __init__(self, api_key: str, lang="en") -> None:
        self.base_url = "https://imdb-api.com"
        self.api_key = api_key
        self.lang = lang

    def url_get(self, call: str, *args):
        url = f"{self.base_url}/{self.lang}/API/{call}/{self.api_key}"

        for arg in args:
            url += f"/{arg}"

        return json.loads(requests.get(url).content)

    def top250_movies(self) -> Top250Movies:
        """
            Get Top 250 Movies.

            Parameters
            ----------
            None

            Returns
            -------
            Top250Movies
        """
        return Top250Movies(self.url_get(ApiCall.Top250Movies))

    def top250_tvs(self) -> MostPopularMovies:
        """
            Get Top 250 Series TVs.

            Parameters
            ----------
            None

            Returns
            -------
            Top250Tvs
        """
        return Top250TVs(self.url_get(ApiCall.Top250TVs))

    def most_popular_movies(self) -> MostPopularMovies:
        """
            Get Top 100 Most Polular Movies.

            Parameters
            ----------
            None

            Returns
            -------
            MostPopularMovies
        """
        return MostPopularMovies(self.url_get(ApiCall.MostPopularMovies))

    def most_popular_tvs(self) -> MostPopularTVs:
        """
            Get Top 100 Most Polular Series TVs.

            Parameters
            ----------
            None

            Returns
            -------
            MostPopularTVs
        """
        return MostPopularTVs(self.url_get(ApiCall.MostPopularTVs))

    def in_theaters(self) -> InTheaters:
        """
        Get In Theaters Movies.

        Parameters
        ----------
        None

        Returns
        -------
        InTheaters
        """
        return InTheaters(self.url_get(ApiCall.InTheaters))

    def comming_soon(self) -> ComingSoon:
        """
            Get Coming Soon Movies.

            Parameters
            ----------
            None

            Returns
            -------
            ComingSoon
        """
        return ComingSoon(self.url_get(ApiCall.ComingSoon))

    def box_office(self) -> BoxOffices:
        """
            Get Weekend Box Office.

            Parameters
            ----------
            None

            Returns
            -------
            BoxOffices
        """
        return BoxOffices(self.url_get(ApiCall.BoxOffice))

    def box_offce_all(self) -> BoxOfficeAll:
        """
            Get Box Office in all times.

            Parameters
            ----------
            None

            Returns
            -------
            BoxOfficeAll
        """
        return BoxOfficeAll(self.url_get(ApiCall.BoxOfficeAllTime))

    def name(self, person_id: str):
        """
            Get information of people (actor, actress, director, writers, ...).

            Parameters
            ----------
            person_id: str
                A valid IMDb Name Id. Id startd withs nm.

            Returns:
                Name
        """
        return Name(self.url_get(ApiCall.Name, person_id))

    def keyword(self, keyword: str) -> Keyword:
        """
            A valid IMDb Keyword (already founded in SearchKeyword action)

            Parameters
            ----------
            keyword: str
                A valid IMDb Keyword (already founded in SearchKeyword action)

            Returns:
                Keyword
        """
        return Keyword(self.url_get(ApiCall.Keyword, keyword))

    def search_movie(self, expression: str) -> SearchMovies:
        """
            Search into all Movies.

            Parameters
            ----------
            expression: str
                Expression for search. For examples "Leon The Professional" or "Inception". You can also SearchMovie with year (ex: "Inception 2010")

            Returns
            -------
            SearchSeries
        """
        return SearchMovies(self.url_get(ApiCall.SearchMovie, expression))

    def search_series(self, expression: str) -> SearchSeries:
        """
            Search into all Series TVs.

            Parameters
            ----------
            expression: str
                Expression for search. For examples "Leon The Professional" or "Inception". You can also SearchMovie with year (ex: "Inception 2010")

            Returns
            -------
            SearchSeries
        """
        return SearchSeries(self.url_get(ApiCall.SearchSeries, expression))

    def title(self, imdb_id: str, options: str = "") -> Title:
        """
            Get Movies or Series TV information.

            Parameters
            ----------
            imdb_id : str
                A valid IMDb Id. Id started withs tt.

            options : str
                Options to get more information about: FullActor, FullCast, Posters, Images, Trailer, Ratings, Wikipedia.

            Returns
            -------
            Title
        """
        return Title(self.url_get(ApiCall.Title, imdb_id, options))

    def search_keword(self, keyword: str) -> SearchKeyword:
        """
        Search into all keywords.

        Parameters
        ----------
        keyword : str
            Expression for search.

        Returns
        -------
        SearchKeyword
        """
        return SearchKeyword(self.url_get(ApiCall.SearchKeyword, keyword))
