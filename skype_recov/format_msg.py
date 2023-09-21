from typing import Optional
from html_wrapper import HtmlWrapper

SEC_IN_MIN = 60
MIN_IN_HR = 60
NO_MSG_CONTENT = "<NO_MESSAGE_CONTENT>"
UNITS = 'hms'

def fmt_duration(sec: Optional[HtmlWrapper]) -> str:
    if sec is None:
        return '0s'

    sec = int(str(sec))
    h, rem = divmod(sec, SEC_IN_MIN * MIN_IN_HR)
    m, s = divmod(rem, SEC_IN_MIN)
    
    parts = [f"{time}{unit}" for time, unit in zip((h, m, s), UNITS) if time]
    return ' '.join(parts)

def get_duration_str(part: Optional[HtmlWrapper]) -> str:
    ident = part['identity']
    duration = fmt_duration(part.duration)
    return f"{ident}'s call duration {duration}."

def format_msg(msg: str) -> str:
    if msg is None:
        return NO_MSG_CONTENT

    if '</' in msg:
        wrapped = HtmlWrapper(msg)
        part_tags = wrapped.find_all('part')  # part tags hold call info

        if part_tags:
            calls = map(get_duration_str, part_tags)
            return ' '.join(calls)

        return wrapped.text.strip()

    return msg
