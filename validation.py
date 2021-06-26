import re
def to_valid(url, VID_ID):
    youtube_urls_test = ['']
    youtube_urls_test.pop(0)
    youtube_urls_test.append(url)
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    youtube_regex_match = re.match(youtube_regex, url)
    VID_ID = youtube_regex_match.group(6)
    if youtube_regex_match != None:
        return VID_ID
    else:
        raise Exception('NOT_VALID_URL')