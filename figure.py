'''
figure 모듈

이 모듈은 Line 클래스와 여러 도형의 넓이를 계산하는 함수를 제공합니다.

클래스:
- Line: 선의 길이를 나타내는 클래스.

함수:
- area_square(line_obj): 정사각형의 넓이를 계산합니다.
- area_circle(line_obj): 원의 넓이를 계산합니다.
- area_regular_triangle(line_obj): 정삼각형의 넓이를 계산합니다.
'''
import math
class Line:
    """Line 클래스

    속성
    ----
        __length : 선의 길이 (기본값: 1). 
            외부에서 접근 불가능한 필드.
            
    메소드
    ------
        __init__(length=1): Line 객체를 초기화합니다.
            유효하지 않은 값이 주어지면 기본값 1로 초기화됩니다.

        set_length(length): __length 필드를 설정합니다.
            유효하지 않은 값이 주어지면 변경되지 않습니다.

        get_length(): __length 필드를 반환합니다.
    """
    __length = 1

    def __init__(self, length = 1):
        """객체를 초기화합니다.

        Parameters
        ----------
            length : int or float, optional (Default: 1).
        
        Returns
        -------
            No returns.
        
        Example
        -------
            >>> myline = figure.Line(10) # 길이를 10으로 설정한다.
        """
        if (type(length) != int and type(length) != float) or (length <= 0):
            self.__length = 1
        else:
            self.__length = length
    
    def set_length(self, length):
        """선의 길이를 설정합니다.

        Parameters
        ----------
            length : int or float, must be positive.

        Returns
        -------
            No returns.
        
        Example
        -------
            >>> myline.set_length(10) # 길이를 10으로 설정한다.
        """
        if not ((type(length) != int and type(length) != float) or (length <= 0)):
            self.__length = length
    
    def get_length(self):
        """선의 길이를 반환합니다.

        Parameters
        ----------
            No parameters.

        Returns
        -------
            length: 현재 선의 길이.

        Example
        -------
            >> myline.get_length() # 다른 값을 변경하지 않으면 Default 값인 1을 반환한다.
        """
        return self.__length
    
def area_square(line_obj):
    """주어진 Line 객체의 길이를 한 변으로 하는 정사각형의 넓이를 계산합니다.

    Parameters
    ----------
        line_obj : Line
            Line 클래스의 객체.

    Returns
    -------
        정사각형의 넓이. 유효하지 않은 Line 객체가 주어지면 0을 반환합니다.

    Example
    -------
        >>> print(area_square(myline)) # length가 10일 때 100을 반환한다.
    """
    if isinstance(line_obj, Line):
        return line_obj.get_length() ** 2
    else:
        return 0

def area_circle(line_obj):
    """주어진 Line 객체의 길이를 반지름으로 하는 원의 넓이를 계산합니다.

    Parameters
    ----------
        line_obj : Line
            Line 클래스의 객체.

    Returns
    -------
        원의 넓이. 유효하지 않은 Line 객체가 주어지면 0을 반환합니다.

    Example
    -------
        >>> print(area_circle(myline)) # length가 10일 때 314.1592653589793을 반환한다.
    """
    if isinstance(line_obj, Line):
        return (line_obj.get_length() ** 2) * math.pi
    else:
        return 0

def area_regular_triangle(line_obj):
    """주어진 Line 객체의 길이를 한 변으로 하는 정삼각형의 넓이를 계산합니다.

    Parameters
    ----------
        line_obj : Line
            Line 클래스의 객체.

    Returns
    -------
        정삼각형의 넓이. 유효하지 않은 Line 객체가 주어지면 0을 반환합니다.
    
    Example
    -------
        >>> print(area_regular_triangle(myline)) # length가 10일 때 43.30127018922193을 리턴한다.
    """
    if isinstance(line_obj, Line):
        return (math.sqrt(3) * (line_obj.get_length() ** 2)) / 4
    else:
        return 0