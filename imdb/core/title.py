class TitleCore:
    def __init__(self, response: dict) -> None:
        self.response = response
        self.id = response.get("id")
        self.title = response.get("title")
        self.original_title = response.get("originalTitle")
        self.full_title = response.get("fullTitle")
        self.type = response.get("type")
        self.year = response.get("year")
        self.image = response.get("image")
        self.release_date = response.get("releaseDate")
        self.runtime_mins = response.get("runtimeMins")
        self.runtime_str = response.get("runtimeStr")
        self.plot = response.get("plot")
        self.plot_local = response.get("plotLocal")
        self.plot_local_is_rtl = response.get("plotLocalIsRtl")
        self.awards = response.get("awards")
        self.directors = response.get("directors")
        self.director_list = response.get("directorList")
        # todo : change this to directors object
        # [{"id": "string", "name": "string"}]
        self.writers = response.get("writers")
        self.writer_list = response.get("writerList")
        # todo : change this to writers object
        # [{"id":"","name": "string"}]
        self.stars = response.get("stars")
        self.star_list = response.get("starList")
        # [{"id":"", "name": "string"}],
        self.actor_list = response.get("actorList")
        # [{"id": "", "image": "", "name": "", "asCharacter": "string"}]
        self.full_cast = response.get("fullCast")
        # {
        #     "imDbId"
        #     "title"
        #     "fullTitle"
        #     "type"
        #     "year"
        #     "directors": {
        #     "job"
        #     "items": [
        #         {
        #         "id"
        #         "name"
        #         "description": "string"
        #         }
        #     ]
        #     },
        #     "writers": {
        #     "job"
        #     "items": [
        #         {
        #         "id"
        #         "name"
        #         "description": "string"
        #         }
        #     ]
        #     },
        #     "actors": [
        #     {
        #         "id"
        #         "image"
        #         "name"
        #         "asCharacter": "string"
        #     }
        #     ],
        #     "others": [
        #     {
        #         "job"
        #         "items": [
        #         {
        #             "id"
        #             "name"
        #             "description": "string"
        #         }
        #         ]
        #     }
        #     ],
        #     "errorMessage": "string"
        # }
        self.genres = response.get("genres")
        self.genre_list = response.get("genreList")
        # [
        #     {
        #     "key"
        #     "value": "string"
        #     }
        # ]
        self.companies = response.get("companies")
        self.company_list = response.get("companyList")
        # [
        #     {
        #     "id"
        #     "name": "string"
        #     }
        # ]
        self.countries = response.get("countries")
        self.country_list = response.get("countryList")
        # [
        #     {
        #     "key"
        #     "value": "string"
        #     }
        # ]
        self.languages = response.get("languages")
        self.language_list = response.get("languageList")
        # [
        #     {
        #     "key"
        #     "value": "string"
        #     }
        # ]
        self.content_rating = response.get("contentRating")
        self.imdb_rating = response.get("imDbRating")
        self.imdb_rating_votes = response.get("imDbRatingVotes")
        self.metacritic_rating = response.get("metacriticRating")
        self.ratings = response.get("ratings")
        # {
        #     "imDbId"
        #     "title"
        #     "fullTitle"
        #     "type"
        #     "year"
        #     "imDb"
        #     "metacritic"
        #     "theMovieDb"
        #     "rottenTomatoes"
        #     "tV_com"
        #     "filmAffinity"
        #     "errorMessage": "string"
        # }
        self.wikipedia = response.get("wikipedia")
        # {
        #     "imDbId"
        #     "title"
        #     "fullTitle"
        #     "type"
        #     "year"
        #     "language"
        #     "titleInLanguage"
        #     "url"
        #     "plotShort": {
        #     "plainText"
        #     "html": "string"
        #     },
        #     "plotFull": {
        #     "plainText"
        #     "html": "string"
        #     },
        #     "errorMessage": "string"
        # }
        self.posters = response.get("posters")
        # {
        #     "imDbId"
        #     "title"
        #     "fullTitle"
        #     "type"
        #     "year"
        #     "posters": [
        #     {
        #         "id"
        #         "link"
        #         "aspectRatio": 0,
        #         "language"
        #         "width": 0,
        #         "height": 0
        #     }
        #     ],
        #     "backdrops": [
        #     {
        #         "id"
        #         "link"
        #         "aspectRatio": 0,
        #         "language"
        #         "width": 0,
        #         "height": 0
        #     }
        #     ],
        #     "errorMessage": "string"
        # },
        self.images = response.get("images")
        # {
        #     "imDbId"
        #     "title"
        #     "fullTitle"
        #     "type"
        #     "year"
        #     "items": [
        #     {
        #         "title"
        #         "image": "string"
        #     }
        #     ],
        #     "errorMessage": "string"
        # }
        self.trailer = response.get("trailer")
        # {
        #     "imDbId"
        #     "title"
        #     "fullTitle"
        #     "type"
        #     "year"
        #     "videoId"
        #     "videoTitle"
        #     "videoDescription"
        #     "thumbnailUrl"
        #     "uploadDate"
        #     "link"
        #     "linkEmbed"
        #     "errorMessage": "string"
        # }
        self.box_office = response.get("boxOffice")
        # {
        #     "budget"
        #     "openingWeekendUSA"
        #     "grossUSA"
        #     "cumulativeWorldwideGross": "string"
        # }
        self.tagline = response.get("tagline")
        self.keywords = response.get("keywords")
        self.keyword_list = response.get("keywordList")
        # [
        #     "string"
        # ]
        self.similars = response.get("similars")
        # [
        #     {
        #     "id"
        #     "title"
        #     "fullTitle"
        #     "year"
        #     "image"
        #     "plot"
        #     "directors"
        #     "stars"
        #     "genres"
        #     "imDbRating": "string"
        #     }
        # ],
        self.tv_series_info = response.get("tvSeriesInfo")
        # {
        #     "yearEnd"
        #     "creators"
        #     "creatorList": [
        #     {
        #         "id"
        #         "name": "string"
        #     }
        #     ],
        #     "seasons": [
        #     "string"
        #     ]
        # }
        self.tv_episode_info = response.get("tvEpisodeInfo")
        # {
        #     "seriesId"
        #     "seriesTitle"
        #     "seriesFullTitle"
        #     "seriesYear"
        #     "seriesYearEnd"
        #     "seasonNumber"
        #     "episodeNumber"
        #     "previousEpisodeId"
        #     "nextEpisodeId": "string"
        # }