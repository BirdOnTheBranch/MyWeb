from src import api

CODEWARS_API_URL = 'https://www.codewars.com/api/v1'
STATS_ENDPOINT = f'{CODEWARS_API_URL}/users/BirdOnTheBranch'


def codewars_info():
    """Returns info from Codewars API"""
    return api.perform_api_request(STATS_ENDPOINT).json()


    def get_codewars_info():
        """Retrieves user statistics from Codewars API"""
        stats = codewars_info()
        codewars = {
                    'username': stats['username'],
                    'honor' : stats['honor'], 
                    'overall_rankname': stats['ranks']['overall']['name'],
                    'challenges_completed': stats['codeChallenges']['totalCompleted'],
                    'languages': stats['ranks']['languages']
                }

        return codewars
