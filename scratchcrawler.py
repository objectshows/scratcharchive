import scratchattach as scratch3
from github import Github
g = Github("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")
repo = g.get_repo("objectshows/scratcharchive")
def flat(lis):
    flatList = []
    # Iterate with outer list
    for element in lis:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList
def crawl(username):
    user = scratch3.get_user(username)
    return user.follower_names(limit=40, offset=0)
def crawllist(abc):
    result = []
    for i in range(0, len(abc)):
        try:
            result.append(crawl(abc[i]))
        except Exception:
            pass
    return flat(result)
def crawler(iteration, username):
    resultt = [username]
    for i in range(0, iteration):
        resultt = crawllist(resultt)
    return resultt
times = 6
FINALE = crawler(times, "Wign199")
# Source - https://stackoverflow.com/a/899149
# Posted by osantana, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-05, License - CC BY-SA 4.0
print("All Done!")
repo.create_file(
    path="/data/crawler.txt",
    message="the scratch archive list",
    content="\n".join(str(item) for item in FINALE)
)
