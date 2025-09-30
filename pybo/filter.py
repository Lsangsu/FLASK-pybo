#에러방지용 지역 찾아주기
import locale
locale.setlocale(locale.LC_ALL, '')

#datetime 객체 문자열 템플릿 필터
def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
    return value.strftime(fmt)