
# LangChain Documentation Helper

A repository for learning LangChain by building a generative ai application.

This is a web application is using a Pinecone as a vectorsotre and answers questions about LangChain 
(sources from LangChain official documentation). 


![Logo](https://github.com/emarco177/documentation-helper/blob/main/static/banner.gif)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PINECONE_API_KEY`
`PINECONE_ENVIRONMENT_REGION`
`OPENAI_API_KEY`

## Run Locally

Clone the project

```bash
  git clone https://github.com/emarco177/documentation-helper.git
```

Go to the project directory

```bash
  cd documentation-helper
```

Download LangChain Documentation
```bash
  mkdir langchain-docs
  wget -r -A.html -P langchain-docs https://langchain.readthedocs.io/en/latest/ 
```

Install dependencies

```bash
  pipenv install
```

Start the flask server

```bash
  streamlit run main.py
```


## Running Tests

To run tests, run the following command

```bash
  pipenv run pytest .
```


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.udemy.com/user/eden-marco/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eden-marco/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.udemy.com/user/eden-marco/)
"#bsks-unibo2" 
