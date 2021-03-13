-- SQL
-- 실행 - 번개 아이콘, Ctrl enter
-- database > table > column > row

-- 현재 어떤 DB가 있는지 보기
SHOW DATABASES;

USE database_name;

-- 데이터베이스 테이블 이름 보기
SHOW TABLES;
-- 데이터베이스 테이블 정보 조회 //
SHOW TABLE STATUS;

-- 테이블의 열 확인
DESCRIBE column_name;
DESC column_name;


-- SELECT 구문 // 데이터 가져오기
SELECT select_expr                   -- 원하는 column, 순서대로 // * all 에스터리스크 // 전체 row, data
    DISTINCT -- 중복제거

FROM table_references                -- table 명

WHERE where_condition                -- 특정조건 행 거르기 할때 // poplution >= 8000000(800만 이상 인구)
    -- 조건 만들 때 연산자 조합 가능
    -- 관계연산자 NOT, AND OR
    -- 조건연산자 // = , < , > , <= , >= , <> , != // str : Country code = 'KOR', int :
    -- 기타 함수는 https://dev.mysql.com/doc/refman/8.0/en/functions.html
    BETWEEN AND OR -- 조합할 때 연속적인 숫자 범위
    city IN('Seoul', 'New York', 'Tokyo') -- 이산적인 값 조건
    LIKE -- 문자열 포함 검색할 때 Ctrl f 같은 느낌
    % -- 몇 글자든 찾기 'Tel %' => Tel aviv 
    _ -- 한 글자 찾기 'KO_' => KOR

    -- Sub Query 쿼리안의 쿼리
    WHERE Country > SOME ( SELECT Country FROM city Where Name = 'seoul') 
                      -- 이것만 하면 'KOR' 괄호안에 넣으면 또 찾는 값이 됨 // 서브쿼리 결과가 둘이 이상이면 에러
          ANY -- OR개념 서브쿼리의 여러개의 결과 중 한가지만 만족해도 가능, SOME과 동일의미, =ANY는 IN과 동일
          ALL -- AND개념 그 결과를 모두 만족해야함 

GROUP BY { column_name | expr | position } -- 
    -- 집계 함수 Aggregate Function
    AVG() -- 평균값 
    MIN() -- 최소값
    MAX() -- 최대값
    COUNT() -- 행의 개수
    COUNT(DISTINCT) -- 중복 제외 행의 개수
    STDEV() -- 표준편차
    VARIANCE() -- 분산
    AS 'NickName' -- 보기좋게 Aliac사용

    HAVING where_condition
        -- where 비슷, 집계함수에 대해 조건 제한하는 편리한 개념, 
        -- HAVING은 반드시 GROUP BY 직후에 나와야함
        GROUP BY CountryCode HAVING MAX(poplution) > 9000000 ---population max값이 90만 초과인 것만 groupby

    ROLLUP
        -- 총합, 중간합계, GROUP BY
    JOIN
        --  DB 내 여러 TABLES의 RECORD 조합, 하나의 테이블, 결과 집합 표현
        -- 조건 필요
        ON city.CountryCode = countrylanguage.CountryCode
            -- 조건 기준   

ORDER BY { column_name | expr | position } ASC, poplution DESC -- 혼합가능
    -- 결과 출력 순서 조절, 기본적으로 오름차순 (ASC), 내림차순은 열이름 뒤에 DESC 표기

LIMIT N -- 출력개수 제한, 상위 N개 // 악성쿼리 개선할 때
 

-- 내장함수
LENGTH() -- 문자열 길이

CONCAT( , , , ) -- 하나의 문자열로 결합 // 하나라도 NULL이 있으면 NULL 반환
LOCATE(찾는 문자열, 찾을 곳 ) -- 찾는 문자열이 처음 나타나는 위치 반환, 존재하지 않으면 0 // 첫인덱스는 1

LEFT(문자열, 지정개수) --문자열 왼쪽부터 지정개수만큼 문자반환
RIGHT(문자열, 지정개수) -- 오른쪽부터 

LOWER(문자열) -- 소문자로
UPPER(문자열) -- 대문자로

REPLACE(해당문자열 , 대상문자열, 바꿀문자 ) -- 특정문자열을 대체문자열로
TRIM(TRAILING '#' FROM '####MYSQL####')  -- 문자열 앞뒤로 자를때
    BOTH -- 전달받은 문자열 양 끝에 존대하는 특정문자제거 // 명시없으면 자동
    LEADING -- 전달받은 문자열 앞에 존대하는 특정문자제거
    TRAILING -- 전달받은 문자열 앞에 존대하는 특정문자제거

FORMAT() --  숫자타입데이터 세자리마다 쉼표넣는 형식, 문자열로 반환으로 변환시켜줌 50,000,000

FLOOR() -- 내림
CEIL() -- 올림
ROUNT() -- 반올림

SQRT() -- 양의 제곱근
POW(밑수, 지수) -- 밑수, 지수 => 거듭제곱
EXP(지수) -- 지수를 받아 e의 거듭제곱 계산
LOG() -- 자연로그값 계산

SIN() --사인값 반환
COS() --코사인값 반환
TAN() -- 탄젠트 값 반환

ABS() -- 절대값 반환
RAND() -- 0.0 이상 1.0 미만 하나의 실수 무작위 생성
    ROUND(RAND()*10, 0)

-- 날짜
NOW() --현재 날짜 시간 YYYY-MM-DD HH:MM:SS, YYYYMMDDHHMMSS
CURDATE() -- 현재 날짜 YYYY-MM-DD, YYYYMMDD
CURTIME() -- 현재 시간 HH:MM:SS, HHMMSS

DATE(NOW())
MONTH(NOW())   -- 0 ~ 12
DAT(NOW())     -- 0 ~ 31
HOUR(NOW())    -- 0 ~ 23
MINUTE(NOW())  -- 0 ~ 59
SECOND(NOW())  -- 0 ~ 59

MONTHNAME() -- 월 이름
DAYNAME()  -- 일 이름

DAYOFWEEK() -- 1일 ~ 7토
DAYOFWEEK() -- 0 ~ 31
DAYOFYEAR() -- 1 ~ 366

DATE_FORMAT()  -- 전달받은 형식에 맞춰 날짜 시간 정보 문자열로 반환


-- 고급
CREATE TABLE city2 AS SELECT * FROM CITY;
-- TABLE 만들기

CREATE DATABASE database_name -- DATABASE 만들기
USE 문으로 새 데이터베이스 사용

CREATE TABLE TEST1(
    ID INT NOT NULL PRIMARY KEY,  -- ID은 INT TYPE, NULL은 올수없고, PRIMARY KEY이다
    COL1 INT NULL, -- INT
    COL2 FLOAT NULL, -- FLOAT
    COL3 VARCHAR(45) NULL --VARIABLE  캐릭터 가변길이 문자열 최대길이 45
)

SELECT * FROM NULL -- 로 확인

ALTER TABLE TEST1 -- 수정할 때
ADD COL4 INT NULL; -- 추가
MODIFY COL4 VARCHAR() NULL -- 수정 
DROP COL4; -- 삭제

INDEX -- 테이블에서 원하는 데이터 빠르게 찾기 위해
-- 전체를 읽지 않고, 검색 많이할 때

CREATE INDEX COL1IDX
ON TEST (COL1)
    UNIQUE -- 중복값 비허용
    FULLTEXT INDEX -- 일반적인과 다르게 매우 빠르게 모든 텍스트 컬럼 검색 // 문자열 탐색할 때
SHOW INDEX FROM TEST;
-- 이때 PRIMARY KEY는 기본적으로 따라옴

ALTER TABLE TEST
DROP INDEX COL1IDX

DROP INDEX COL1IDX ON TEST

VIEW -- 가상 테이블, 필요한 것만, 단순화, 재사용,  
    -- 기존 방식과 동일하게 적용

INSERT INTO TEST
VALUE(1, 123, 101, 'TEST', 1.1)
-- COLOMN 수와 같게 삽입

-- TABLE에 직접 입력가능 -- APPLY 클릭
INSERT INTO TEST2 SELECT * FROM TEST -- 복사하기

-- ROW 그대로 변경
UPDATE TEST
SET COL1 = 1, COL2 = 1.0, COL3 = 'TEST'
WHERE ID = 1;

DELETE FROM 테이블
-- 데이터는 지워지지만 용량자체는 지워지지 않음, 롤백가능하기 때문

DROP TABLE -- 복구불가
DROP DATABASE
TRUNCATE -- 복구불가




