import pygame    # To play sound
import time      # To make a break while a sound is playing to avoid collision
pygame.init()

# Global variables for the integer_to_vietnamese_numeral function
ti = 'tỷ'                         
trieu = 'triệu'                  
nghin = 'nghìn'                  
tram = 'trăm'
muoi = 'mươi'
mot = 'mốt'
khong = 'linh'

# Global variables for the integer_to_english_numeral function
billion = 'billion'
million = 'million'
thousand = 'thousand'
hundred = 'hundred'
teen = 'teen'
zero = 'and'

# Replace global variables of the integer_to_vietnamese_numeral function when region is South
def southern():
    global nghin
    global khong
    nghin = 'ngàn'
    khong = 'lẻ'

# Replace global variables of the integer_to_vietnamese_numeral function when region is North
def northern():
    global nghin
    global khong
    nghin = 'nghìn'
    khong = 'linh'

# Check if the number is from 1 - 9
def check_case(n):
    case = ['1','2','3','4','5','6','7','8','9']
    if n in case: return True
    elif n not in case: return False

# Check if the number is from 0 - 9
def check_int(n):
    num = ['0','1','2','3','4','5','6','7','8','9']
    for i in n:
        if i in num: pass
        elif i not in num: return False
    return True

# Check if the number contains zeros
def check_zero(n):
    for i in n:
        if i == '0': pass
        elif i != '0': return False
    return True

# Check if the number is '1'
def check_one(n):
    if n == '1': return True
    else: return False

# Check if the number is '5'
def check_five(n):
    if n == '5': return True
    else: return False

# Function read number in hundred from number's groups in Vietnamese 
def hundreds(num):
    lstnm = {
    '1': 'một',
    '2': 'hai',
    '3': 'ba',
    '4': 'bốn',
    '5': 'năm',
    '6': 'sáu',
    '7': 'bảy',
    '8': 'tám',
    '9': 'chín',
        }

    lstn = {
    '0': 'không',
    '1': 'một',
    '2': 'hai',
    '3': 'ba',
    '4': 'bốn',
    '5': 'năm',
    '6': 'sáu',
    '7': 'bảy',
    '8': 'tám',
    '9': 'chín'
        }

    lstsp = {
    '1': 'mười',
    '5': 'lăm'
        }

    tram = 'trăm'
    num = str(num)
    if len(num) == 1: 
        if check_zero(num[0]): raise ValueError('0 is a neutrual integer')
        else:             # Nếu chỉ có 1 chữ số
            res = lstnm[num[0]]        # Trả về chữ số trong lstnm
            return res
    elif len(num) == 2:                          # Nếu như có 2 chữ số
        if check_one(num[0]):                    # Nếu như chữ số đầu tiên là số 1
            if check_zero(num[1]):               # Nếu như chữ số thứ 2 là số 0
                res = lstsp[num[0]]              # Trả về giá trị 'mười' trong lstsp
                return res
            elif check_five(num[1]):                                # Nếu như chữ số thứ 2 là số 5       (vd: 15)
                res = lstsp[num[0]],lstsp[num[1]]                   # Trả về 'mười lăm' với num[0] là mười và num[1] là lăm trong lstsp
            else:
                res = lstsp[num[0]],lstnm[num[1]]                   # Trả về num[0] trong lstsp ('mười') với num[1] trong lstnm
        elif not check_one(num[0]) and check_case(num[0]):          # Nếu như số đầu không phải 1 mà nằm trong khoảng từ 1-9:   
            if check_one(num[1]):                                   # Nếu số thứ 2 là số 1       (vd: 21)
                res = lstnm[num[0]],muoi,mot                        # Trả về số đầu (num[0]) trong lstnm và 'mươi','mốt'
            elif check_zero(num[1]):                                # Nếu như số thứ 2 là số 0      (vd: 50)
                res = lstnm[num[0]],muoi                            # Trả về số đầu (num[0]) trong lstnm và 'mươi'
            elif check_five(num[1]):                                # Nếu như số thứ 2 là 5       (vd: 25)
                res = lstnm[num[0]],muoi,lstsp[num[1]]              # Trả về số đầu (num[0]) trong lstnm và 'mươi',num[1] trong lstsp là 'lăm'
            else:
                res = lstnm[num[0]],muoi,lstnm[num[1]]              # Trả về giá trị số đầu (num[0]) trong lstnm,'mươi',num[1] trong lstnm 
    elif len(num) == 3:                                                                 # Nếu như có 3 chữ số                    
        if check_zero(num):                                                             # Nếu như cả 3 chữ số đều là số 0
            res = ''                                                                    # Trả về khoảng trống
            return res
        elif check_zero(num[1:]):                                                       # Nếu như 2 chữ số sau cùng là số 0       (vd: 200)
            res = lstnm[num[0]],tram                                                    # Trả về chữ số đầu trong lstnm, 'trăm'
        elif check_zero(num[1]) and check_case(num[-1:]):                               # Nếu như chữ số thứ 2 là 0 và chữ số thứ 3 từ 1-9
            if check_case(num[0]):                                                      # Nếu như số đầu tiên từ 1-9       (vd: 502)
                res = lstnm[num[0]],tram,khong,lstnm[num[-1:]]                          # Trả về num[1], 'trăm', 'linh', chữ số cuối trong lstnm
            elif check_zero(num[0]):                                                    # Nếu như số đầu tiên là 0       (vd: 007)
                res =lstn[num[0]],tram,khong,lstnm[num[-1:]]                            # Trả về 0, 'trăm', 'linh', chữ số cuối trong lstnm
        elif check_zero(num[0]) and check_case(num[1]) and check_zero(num[-1:]):        # Nếu như chữ số đầu là 0, chữ số thứ 2 từ 1-9 và chữ số thứ 3 là 0      (vd: 210)
            res =lstn[num[0]],tram,lstnm[num[1]],muoi                                   # Trả về chữ số đầu num[0], 'trăm', chữ số 2 num[1], 'mười'
        elif check_case(num[1]) and check_zero(num[-1:]):                               # Nếu như số thứ 2 từ 1-9 và số cuối là 0     
            if check_one(num[1]):                                                       # Nếu như số thứ 2 là 1      (vd: 410)
                res = lstnm[num[0]],tram,lstsp[num[1]]                                  # Trả về số đầu tiên num[0], 'trăm', số thứ 2 num[1] trong lstsp
            elif check_case(num[1]) and not check_one(num[1]):                          # Nếu như chữ số thứ 2 từ 1 tới 9 và không phải là 1      (vd: 750)
                res = lstnm[num[0]],tram,lstnm[num[1]],muoi                             # Trả về số đầu tiên num[0], 'trăm', số thứ 2 num[1], 'mươi'
        elif check_zero(num[0]) and check_case(num[1]) and check_case(num[-1:]):        # Nếu số đầu là 0 và số thứ 2,3 từ 1-9
            if check_one(num[1]):                                                       # Nếu như số thứ 2 là 1
                if check_zero(num[-1:]):                                                # Nếu như số cuối là 0     (vd: 010)
                    res =lstn[num[0]],tram,lstsp[num[1]]                                # Trả về số đầu tiên num[0], 'trăm', số thứ 2 num[1] torng lstsp
                elif check_five(num[-1:]):                                              # Nếu như số cuối là 5       (vd: 015)
                    res =lstn[num[0]],tram,lstsp[num[1]],lstsp[num[-1:]]                # Trả về số đầu tiên num[0], 'trăm', số thứ 2 num[1] trong lstsp và số thứ 3 num[2] trong lssp
                else:
                    res =lstn[num[0]],tram,lstsp[num[1]],lstnm[num[-1:]]                # Trả về số đầu tiên num[0], 'trăm', số thứ 2 num[1] trong lstsp và số thứ 3 trong lstnm
            else:
                if check_zero(num[-1:]):                                                # Nếu như số cuối cùng là 0       (vd: 050)
                    res =lstn[num[0]],tram,lstnm[1],muoi                                # Trả về số đầu tiên num[0], 'trăm', số thứ 2 num[1], 'mươi'
                elif check_one(num[-1:]):                                               # Nếu như số cuối cùng là số 1     (vd: 021)
                    res =lstn[num[0]],tram,lstnm[num[1]],muoi,mot                       # Trả về số đầu tiên num[0], 'trăm', số thứ 2 trong lstnm, 'mươi', 'mốt'
                elif check_five(num[-1:]):                                              # Nếu như số cuối là 5       (vd: 025)
                    res =lstn[num[0]],tram,lstnm[num[1]],muoi,lstsp[num[-1:]]           # Trả về số đầu tiên num[0] trong lstnm, 'trăm', số thứ 2 num[1] trong lstnm, 'mươi', số cuối trong lstsp
                else:
                    res =lstn[num[0]],tram,lstnm[num[1]],muoi,lstnm[num[-1:]]           # Trả về số đầu tiên num[0], 'trăm', số thứ 2 num[1], 'mươi' và số thứ 3 num[-1:] trong lstnm
        elif check_one(num[1]) and check_case(num[-1:]):                                # Nếu số thứ 2 là 1 và số cuối từ 1-9
            if check_five(num[-1]):                                                     # Nếu số cuối là 5    (vd: 215)
                res = lstnm[num[0]],tram,lstsp[num[1]],lstsp[num[-1:]]                  # Trả về số đầu tiên num[0], 'trăm', số thứ 2 num[1] trong lstsp và số cuối trong lstsp
            else:
                res = lstnm[num[0]],tram,lstsp[num[1]],lstnm[num[-1:]]                  # Trả về số đầu tiên num[0], 'trăm', số thứ 2 num[1] trong lstsp và số cuối trong lst nm
        elif check_case(num[1]) and check_case(num[2]):                                 # Nếu như số thứ 2 và thứ 3 trong khoảng từ 1-9
            if check_one(num[-1]):                                                      # Nếu như số cuối là 1   
                res = lstnm[num[0]],tram,lstnm[num[1]],muoi,mot                         # Trả về số đầu, 'trăm', số thứ 2, 'mươi', 'mốt
            elif check_five(num[-1]):                                                   # Nếu như số cuối là số 5
                res = lstnm[num[0]],tram,lstnm[num[1]],muoi,lstsp[num[-1:]]             # Trả về số đầu, 'trăm', số thứ 2, 'mươi', số thứ 3 trong lstsp
            else:
                res = lstnm[num[0]],tram,lstnm[num[1]],muoi,lstnm[num[-1:]]             # Trả về số đầu, 'trăm', số thứ 2, 'mươi' ,số cuối trong lstnm
        
    # Result return in tuple, convert it into list and then make it a string
    res = list(res)
    res = ' '.join(res)
    return res

# for i in range(1,1000):
#     print(hundreds(i))

# print(hundreds())

# Function read number in hundred from number's groups in English
def hundreds_eng(num):
    lstnm2 = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',                                                         # Cách làm cái tiếng Anh cũng giống 
    '7': 'seven',                                                       # cái ở trên mà trong tiếng Anh nó có nhiều 
    '8': 'eight',                                                       # ngoại lệ hơn như tui đã nói với ông
    '9': 'nine',                                                        # gồm số 11, 12, 13, 15 và đã đc thêm vào
    '10': 'ten',                                                        # dictionary nên chỉ cần gọi nó ra thôi
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '15': 'fifteen'
        }

    lstsp2 = {
    '2': 'twenty-',
    '3': 'thirty-',
    '4': 'forty-',
    '5': 'fifty-',
    '6': 'sixty-',
    '7': 'seventy-',
    '8': 'eighty-',
    '9': 'ninety-'
        }

    num = str(num)
    if len(num) == 1:
        if check_zero(num[0]): raise ValueError('0 is a neutrual integer')
        else:
            res = lstnm2[num[0]]
            return res
    elif len(num) == 2:
        if check_one(num[0]):
            if num in lstnm2:
                res = lstnm2[num]
                return res
            else:
                res = lstnm2[num[1]]+teen
                return res
        elif check_zero(num[1]):
            res = lstsp2[num[0]].replace('-','')
            return res
        else:
            res = lstsp2[num[0]]+lstnm2[num[1]]
            return res
    elif len(num) == 3:
        if check_zero(num):
            res = ''
            return res
        elif check_zero(num[0]):
            if check_zero(num[1]) and check_case(num[-1:]):
                res = lstnm2[num[-1:]]
                return res
            elif check_case(num[1]) and check_case(num[-1:]):
                if num[1:] in lstnm2:
                    res = lstnm2[num[1:]]
                    return res
                elif check_one(num[1]):
                    res = lstnm2[num[-1:]]+teen
                    return res
                else:
                    res = lstsp2[num[1]]+lstnm2[num[-1:]]
                    return res
            elif check_case(num[1]) and check_zero(num[-1:]):
                if num[1:] in lstnm2:
                    res = lstnm2[num[1:]]
                    return res
                else:
                    res = lstsp2[num[1]].replace('-','')
                    return res
        elif check_zero(num[1:]):
            res = lstnm2[num[0]],hundred
        elif check_one(num[1]):
            if num[1:] in lstnm2:
                res = lstnm2[num[0]],hundred,zero,lstnm2[num[1:]]
            else:
                res = lstnm2[num[0]],hundred,zero,lstnm2[num[-1:]],teen
        elif check_case(num[1]) and check_zero(num[-1:]):
            res = lstnm2[num[0]],hundred,zero,lstsp2[num[1]].replace('-','')
        elif check_case(num[1]) and check_case(num[-1:]):
            res = lstnm2[num[0]],hundred,zero,lstsp2[num[1]]+lstnm2[num[-1:]]
        elif check_zero(num[1]) and check_case(num[-1:]):
            res = lstnm2[num[0]],hundred,zero,lstnm2[num[-1:]]
           
    res = list(res)
    res = ' '.join(res)
    return res

# for i in range(1,1000):
#     print(hundreds_eng(i))

# print(hundreds_eng())

# Main function convert integer to VN numeral with 3 arguments (num, region, activate_tts)
def integer_to_vietnamese_numeral(num, region = 'north', activate_tts = False):
    regions = ['north', 'south']        # List of available regions
    if isinstance(region,str) is False:
        raise TypeError('Argument "region" is not a string')
    if region.lower() not in regions:
        raise ValueError('Argument "region" has not a correct value')
    if region.lower() == 'south':
        minus = str(num)
        if len(str(num)) > 12:
            raise OverflowError('Integer greater than 999,999,999,999')
        if isinstance(num,int) is False:
            raise TypeError('Not an integer')
        if isinstance(activate_tts, bool) is False:
            raise TypeError('activate_tts is not a boolean')
        if minus[0] == '-':
            raise ValueError('Not a positive integer')
        southern()
        ans = []
        fnum = '{:,}'.format(num)
        fnum = fnum.split(',')
        if len(str(num)) > 0 and len(str(num)) <= 3:                                        # Còn nguyên khúc này từ đây
            ans = hundreds(fnum[0])                                                         # trở xuống là mấy trường hợp
            if activate_tts == True:                                                        # có số 0 vào trong, như là
                ans = ans.split(' ')                                                        # 2006000000 thì nó sẽ bỏ cách đọc
            else:                                                                           # của mấy số 0 mà thay vào đó là
                return ans                                                                  # khoảng trăng giống cái if đầu
        elif len(str(num)) > 3 and len(str(num)) <= 6:                                      # tiên trong len 3 á, còn lại thì chứ
            if check_zero(fnum[1]):                                                         # hundred + tỷ + hundred + triệu + ...
                ans = hundreds(fnum[0]),nghin
            else:
                ans = hundreds(fnum[0]),nghin,hundreds(fnum[1])
        elif len(str(num)) > 6 and len(str(num)) <= 9:
            if check_zero(fnum[1]) and check_zero(fnum[2]):
                ans = hundreds(fnum[0]),trieu
            elif check_zero(fnum[1]):
                ans = hundreds(fnum[0]),trieu,hundreds(fnum[2])
            else:
                ans = hundreds(fnum[0]),trieu,hundreds(fnum[1]),nghin,hundreds(fnum[2])
        elif len(str(num)) > 9 and len(str(num)) <= 12:
            if check_zero(fnum[1]) and check_zero(fnum[2]) and check_zero(fnum[3]):
                ans = hundreds(fnum[0]),ti
            elif check_zero(fnum[1]) and check_zero(fnum[2]) and check_int(fnum[3]):
                ans = hundreds(fnum[0]),ti,hundreds(fnum[3])
            elif check_zero(fnum[1]) and check_int(fnum[2]) and check_int(fnum[3]):
                ans = hundreds(fnum[0]),ti,hundreds(fnum[2]),nghin,hundreds(fnum[3])
            elif check_int(fnum[1]) and check_int(fnum[2]) and check_zero(fnum[3]):
                ans = hundreds(fnum[0]),ti,hundreds(fnum[1]),trieu,hundreds(fnum[2]),nghin
            elif check_int(fnum[1]) and check_zero(fnum[2]) and check_int(fnum[3]):
                ans = hundreds(fnum[0]),ti,hundreds(fnum[1]),trieu,hundreds(fnum[3])
            elif check_int(fnum[1]) and check_zero(fnum[2]) and check_zero(fnum[3]):
                ans = hundreds(fnum[0]),ti,hundreds(fnum[1]),trieu
            elif check_zero(fnum[1]) and check_int(fnum[2]) and check_zero(fnum[3]):
                ans = hundreds(fnum[0]),ti,hundreds(fnum[2]),nghin
            else:
                ans = hundreds(fnum[0]),ti,hundreds(fnum[1]),trieu,hundreds(fnum[2]),nghin,hundreds(fnum[3])
            
    elif region.lower() == 'north':
        minus = str(num)
        if len(str(num)) > 12:
            raise OverflowError('Integer greater than 999,999,999,999')
        if isinstance(num,int) is False:
            raise TypeError('Not an integer')
        if isinstance(activate_tts, bool) is False:
            raise TypeError('activate_tts is not a boolean')
        if minus[0] == '-':
            raise ValueError('Not a positive integer')
        northern()
        ans = []
        fnum = '{:,}'.format(num)
        fnum = fnum.split(',')
        if len(str(num)) > 0 and len(str(num)) <= 3:
            ans = hundreds(fnum[0])
            if activate_tts == True:
                ans = ans.split(' ')
            else:
                return ans
        elif len(str(num)) > 3 and len(str(num)) <= 6:
            if check_zero(fnum[1]):
                ans = hundreds(fnum[0]),nghin
            else:
                ans = hundreds(fnum[0]),nghin,hundreds(fnum[1])
        elif len(str(num)) > 6 and len(str(num)) <= 9:
            if check_zero(fnum[1]) and check_zero(fnum[2]):
                ans = hundreds(fnum[0]),trieu
            elif check_zero(fnum[1]):
                ans = hundreds(fnum[0]),trieu,hundreds(fnum[2])
            else:
                ans = hundreds(fnum[0]),trieu,hundreds(fnum[1]),nghin,hundreds(fnum[2])
        elif len(str(num)) > 9 and len(str(num)) <= 12:
            if check_zero(fnum[1]) and check_zero(fnum[2]) and check_zero(fnum[3]):
                ans = hundreds(fnum[0]),ti
            elif check_zero(fnum[1]) and check_zero(fnum[2]) and check_int(fnum[3]):
                ans = hundreds(fnum[0]),ti,hundreds(fnum[3])
            elif check_zero(fnum[1]) and check_int(fnum[2]) and check_int(fnum[3]):
                ans = hundreds(fnum[0]),ti,hundreds(fnum[2]),nghin,hundreds(fnum[3])
            elif check_int(fnum[1]) and check_int(fnum[2]) and check_zero(fnum[3]):
                ans = hundreds(fnum[0]),ti,hundreds(fnum[1]),trieu,hundreds(fnum[2]),nghin
            elif check_int(fnum[1]) and check_zero(fnum[2]) and check_int(fnum[3]):
                ans = hundreds(fnum[0]),ti,hundreds(fnum[1]),trieu,hundreds(fnum[3])
            elif check_int(fnum[1]) and check_zero(fnum[2]) and check_zero(fnum[3]):
                ans = hundreds(fnum[0]),ti,hundreds(fnum[1]),trieu
            elif check_zero(fnum[1]) and check_int(fnum[2]) and check_zero(fnum[3]):
                ans = hundreds(fnum[0]),ti,hundreds(fnum[2]),nghin
            else:
                ans = hundreds(fnum[0]),ti,hundreds(fnum[1]),trieu,hundreds(fnum[2]),nghin,hundreds(fnum[3])

    ans = list(ans)
    if '' in ans:
        ans.remove('')
    ans = ' '.join(ans)

    if activate_tts == True:
        if region.lower() == 'north':
            ans = ans.split(' ')
            pygame.display.set_mode((200,100))
            for word in ans:
                speech = 'sounds//vie//north//'+word.lower()+'.ogg'       # Path to the sound file
                pygame.mixer.music.load(speech)
                pygame.mixer.music.play(0)
                time.sleep(3/4)     # Break the sound for 0.75 sec unless it will be crashed
            ans = ' '.join(ans)
            return ans
        elif region.lower() == 'south':
            ans = ans.split(' ')
            pygame.display.set_mode((200,100))
            for word in ans:
                speech = 'sounds//vie//south//'+word.lower()+'.ogg'       # Path to the sound file
                pygame.mixer.music.load(speech)
                pygame.mixer.music.play(0)
                time.sleep(3/4)     # Break the sound for 0.75 sec unless it will be crashed
            ans = ' '.join(ans)
            return ans
    else:
        return ans

# Test Vietnamese number generation
# for i in range(1,1000000000000):
#     print(integer_to_vietnamese_numeral(i,region='South'))     

# Main function convert integer to English numeral with 2 arguments(num, activate_tts)
def integer_to_english_numeral(num, activate_tts = False):
    minus = str(num)
    if isinstance(num, int) is False:
        raise TypeError('Not an integer')
    if len(str(num)) > 12:
        raise OverflowError('Integer greater than 999,999,999,999')
    if isinstance(activate_tts, bool) is False:
        raise TypeError('activate_tts is not a boolean')
    if minus[0] == '-':
        raise ValueError('Not a positive integer')
    ans = []
    fnum = '{:,}'.format(num)
    fnum = fnum.split(',')
    if len(str(num)) > 0 and len(str(num)) <= 3:
        ans = hundreds_eng(fnum[0])
        if activate_tts == True:
            ans = ans.split(' ')
        else: 
            return ans
    elif len(str(num)) > 3 and len(str(num)) <= 6:
        if check_zero(fnum[1]):
            ans = hundreds_eng(fnum[0]),thousand
        else:
            ans = hundreds_eng(fnum[0]),thousand,zero,hundreds_eng(fnum[1])
    elif len(str(num)) > 6 and len(str(num)) <= 9:
        if check_zero(fnum[1]) and check_zero(fnum[2]):
            ans = hundreds_eng(fnum[0]),million
        elif check_zero(fnum[1]):
            ans = hundreds_eng(fnum[0]),million,zero,hundreds_eng(fnum[2])
        else:
            ans = hundreds_eng(fnum[0]),million,hundreds_eng(fnum[1]),thousand,zero,hundreds_eng(fnum[2])
    elif len(str(num)) > 9 and len(str(num)) <= 12:
        if check_zero(fnum[1]) and check_zero(fnum[2]) and check_zero(fnum[3]):
            ans = hundreds_eng(fnum[0]),billion
        elif check_zero(fnum[1]) and check_zero(fnum[2]) and check_int(fnum[3]):
            ans = hundreds_eng(fnum[0]),billion,zero,hundreds_eng(fnum[3])
        elif check_zero(fnum[1]) and check_int(fnum[2]) and check_int(fnum[3]):
            ans = hundreds_eng(fnum[0]),billion,hundreds_eng(fnum[2]),thousand,zero,hundreds_eng(fnum[3])
        elif check_int(fnum[1]) and check_int(fnum[2]) and check_zero(fnum[3]):
            ans = hundreds_eng(fnum[0]),billion,hundreds_eng(fnum[1]),million,hundreds_eng(fnum[2]),thousand
        elif check_int(fnum[1]) and check_zero(fnum[2]) and check_int(fnum[3]):
            ans = hundreds_eng(fnum[0]),billion,hundreds_eng(fnum[1]),million,zero,hundreds_eng(fnum[3])
        elif check_int(fnum[1]) and check_zero(fnum[2]) and check_zero(fnum[3]):
            ans = hundreds_eng(fnum[0]),billion,hundreds_eng(fnum[1]),million
        elif check_zero(fnum[1]) and check_int(fnum[2]) and check_zero(fnum[3]):
            ans = hundreds_eng(fnum[0]),billion,hundreds_eng(fnum[2]),thousand
        else:
            ans = hundreds_eng(fnum[0]),billion,hundreds_eng(fnum[1]),million,hundreds_eng(fnum[2]),thousand,zero,hundreds_eng(fnum[3])

    ans = list(ans)
    if '' in ans:
        ans.remove('')
    ans = ' '.join(ans)
    ans = ans.replace('-',' ')

    if activate_tts == True:
        ans = ans.split(' ')              
        pygame.display.set_mode((200,100))
        for word in ans:
            speech = 'sounds//eng-US//'+word.lower()+'.mp3'       # Path to the sound file
            pygame.mixer.music.load(speech)
            pygame.mixer.music.play(0)
            time.sleep(3/4)     # Break the sound for 0.75 sec unless it will be crashed
        ans = ' '.join(ans)
        return ans
    else: 
        return ans

# Test English number generation
# for i in range(1,1000000000000):
#     print(integer_to_english_numeral(i))

print(integer_to_vietnamese_numeral(1011,region='south',activate_tts=False))
print(integer_to_vietnamese_numeral(1001,region='south',activate_tts=False))

print(integer_to_vietnamese_numeral(1011,region='north',activate_tts=False))
print(integer_to_vietnamese_numeral(1001,region='north',activate_tts=False))

print(integer_to_english_numeral(1011,activate_tts=False))
print(integer_to_english_numeral(1001,activate_tts=False))