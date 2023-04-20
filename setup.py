from setuptools import setup, find_packages

setup(
    name="pyEasyChatGPT",   # pypi 에 등록할 라이브러리 이름
    version="0.1.1",    # pypi 에 등록할 version (수정할 때마다 version up을 해줘야 함)
    description="An unofficial Python wrapper for OpenAI's ChatGPT API form pyChatGPT",
    author="jaewoo-so",
    author_email="nchos88@gmail.com",
    url="https://github.com/jaewoo-so/pyEasyChatGPT",
    python_requires=">= 3.8",
    keywords=['chatgpt', 'pychatgpt','gpt','openai'],
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    # 중요한 부분
    package_data={},
    include_package_data=True
)