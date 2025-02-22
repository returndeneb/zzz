멀티모달 AI 기반 방송 감시 및 캡션 생성 프로젝트

📌 프로젝트 개요

이 프로젝트는 네이버 치지직 방송을 감시하고, 영상을 다운로드한 후 원하는 이미지를 추출하여 크롤링한 데이터와 채팅 로그를 활용해 AI 모델을 학습시키는 멀티모달 머신러닝 프로젝트입니다. 최종적으로 새로운 이미지가 생성될 때 자동으로 캡션을 생성하는 기능을 포함합니다.




🛠 주요 기능

1️⃣ 치지직 방송 감시 시스템

특정 방송이 시작되었는지 실시간 감시

방송이 켜지면 신호를 보내는 기능 구현

2️⃣ 영상 다운로드 시스템

감시된 방송을 자동으로 다운로드

M3U8 스트리밍 방식 지원

FFmpeg 및 yt-dlp를 활용한 다운로드 기능 구현

3️⃣ 이미지 추출 시스템

다운로드한 영상에서 원하는 장면(완성된 그림) 추출

OpenCV 및 FFmpeg를 이용하여 특정 프레임을 추출하는 기능 구현

![로고](https://github.com/returndeneb/zzz/blob/main/Screens.png)


4️⃣ 이미지 및 캡션 크롤링 시스템

이미 업로드된 이미지 및 캡션 데이터 크롤링

웹 스크래핑을 통해 데이터를 수집하고 학습 데이터셋 구축

5️⃣ 채팅 로그 수집 시스템

방송 중의 채팅 데이터를 수집하여 텍스트 로그 저장

(외부 프로젝트 활용) API 또는 크롤링을 통해 채팅 저장 https://github.com/Buddha7771/ChzzkChat

6️⃣ 머신러닝 기반 자동 캡션 생성 시스템

수집한 이미지 + 캡션 + 채팅 로그를 활용한 멀티모달 학습

CLIP 모델 기반으로 새로운 이미지에 대한 캡션 생성

OpenAI CLIP 및 PyTorch를 활용한 모델 파인튜닝


Python, PyTorch, OpenAI CLIP, OpenCV, FFmpeg, yt-dlp

BeautifulSoup, Selenium, Requests (웹 크롤링)

Transformers, Multimodal Learning (머신러닝)
