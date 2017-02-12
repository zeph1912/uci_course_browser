import urllib.request as urllib_req
import urllib.parse as urllib_parse
import time
from os import system


def ring(time_count:int)->None:
    for i in range(time_count):
        system('afplay /System/Library/Sounds/Glass.aiff')


def Send_Request(Dep,CNum:str)->None:
    course_data = { \
        'Submit':'Display Text Results',
        'YearTerm':'2016-92',
        'ShowComments':'on',
        'ShowFinals':'on',
        'Breadth':'ANY',
        'Dept':Dep,
        'CourseNum':CNum,
        'Division':'ANY',
        'ClassType':'ALL',
        'FullCourses':'ANY',
        'FrontSize':'100',
        'CancelledCourses':'Exclude',
    }

    ascii_data = urllib_parse.urlencode(course_data).encode('Ascii')

    course_req = urllib_req.Request( \
        url = 'http://www.reg.uci.edu/perl/WebSoc',
        data = ascii_data
    )
    result = urllib_req.urlopen(course_req).read()

    for result_line in str(result).split('\\n'):
        if result_line != '' and '***' not in result_line:
            print(result_line)
        if '***' in result_line:
            print(result_line)
            break

    if 'OPEN' in str(result):
        print('   #########################################################################')
        print('   ###  {:10s} is open!!!                                            ###'. \
            format(Dep + ' ' + CNum))
        print('   #########################################################################')
        ring(10)


while True:
    Send_Request('ARTS','1')
  #  Send_Request('MATH','121A')
    time.sleep(65)
