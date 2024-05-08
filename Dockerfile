# 이미지를 만들 수 있는 명령어들의 집합
# app은 앱경로로 이동하는 거
# copy는 app폴더로 카피
# 그 다음에 실행
# 그 다음에 모든 파일을 복사 워킹디렉토리로 복사해달라는 것
# 커맨드를 실행 서버구동 커맨드 명령어
FROM python:3.8-slim-buster
RUN apt-get update
#apt-get update 명령어는 Ubuntu 패키지 저장소의 패키지 목록을 업데이트합니다.
#이를 통해 최신 버전의 패키지 정보를 얻을 수 있습니다.
#도커 이미지 빌드 시 이 명령어를 실행하면 이미지에 최신 패키지 정보가 포함됩니다.
RUN apt-get install -y gcc
#apt-get install -y gcc 명령어는 GNU Compiler Collection(GCC) 컴파일러를 설치합니다.
#GCC는 C, C++, Fortran 등 다양한 프로그래밍 언어를 컴파일할 수 있는 컴파일러 도구입니다.
#-y 옵션은 설치 과정에서 사용자 입력 없이 자동으로 진행하도록 합니다.
RUN apt-get install -y default-libmysqlclient-dev
# apt-get install -y default-libmysqlclient-dev 명령어는 MySQL 클라이언트 라이브러리 개발 패키지를 설치합니다.
#이 패키지는 MySQL 데이터베이스와 상호작용하는 애플리케이션 개발에 필요한 헤더 파일과 라이브러리를 제공합니다.
#예를 들어 Python의 MySQL 연동 라이브러리인 mysqlclient를 사용하려면 이 패키지가 필요합니다.
RUN apt-get update && apt-get install -y pkg-config
ENV PYTHONBUFFERED 1
#ENV PYTHONBUFFERED 1 명령어는 Python 애플리케이션의 출력 버퍼링을 비활성화합니다.
#이를 통해 Python 애플리케이션의 출력이 실시간으로 표시되도록 합니다.
#디버깅이나 로깅 등에 유용할 수 있습니다.

WORKDIR /app/E:/portpolio/carbon_industry/carbonindustry

COPY requirements.txt /app/E:/portpolio/carbon_industry/carbonindustry

RUN pip3 install -r requirements.txt

COPY ./ ./E:/portpolio/carbon_industry/carbonindustry
WORKDIR /app/E:/portpolio/carbon_industry/carbonindustry
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]