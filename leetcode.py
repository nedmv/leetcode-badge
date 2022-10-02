from dataclasses import dataclass
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

class LeetcodeUserdata():
  def __init__(self, name: str):
    self.name = name
    data = self.query()

    total_data = data['allQuestionsCount']
    for item in total_data:
      match(item['difficulty']): 
        case 'All':
          self.total = item['count']
        case 'Easy':
          self.total_easy = item['count']
        case 'Medium':
          self.total_medium = item['count']
        case 'Hard':
          self.total_hard = item['count']

    userdata = data['matchedUser']['submitStats']['acSubmissionNum']
    for item in userdata:
      match(item['difficulty']):
        case 'All':
          self.user_total = item['count']
          self.submissions = item['submissions']
        case 'Easy':
          self.user_easy = item['count']
          self.submissions_easy = item['submissions']
        case 'Medium':
          self.user_medium = item['count']
          self.submissions_medium = item['submissions']
        case 'Hard':
          self.user_hard = item['count']
          self.submissions_hard = item['submissions']

  def query(self):
    LEETCODE_GRAPHQL_URL="https://leetcode.com/graphql"
    transport = AIOHTTPTransport(url=LEETCODE_GRAPHQL_URL)
    client = Client(transport=transport)
    query = gql(
        """
      query getUserProfile($user: String!) {
        allQuestionsCount {
          difficulty
          count
        }
        matchedUser(username: $user) {
          submitStats {
            acSubmissionNum {
              difficulty
              count
              submissions
            }
          }
        }
      }
    """
    )
    query_params = {'user': self.name}
    return client.execute(query, variable_values=query_params)