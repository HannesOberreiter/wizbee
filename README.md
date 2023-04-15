# WizBee

Simple answer bot integrated into [https://www.btree.at/](b.tree Beekeeping Software). This repository is a playground, currently the main goal is to upload the markdown documentation to a vector database.

## Setup

As vector database a Docker redis instance is used, see [https://github.com/HannesOberreiter/btree_database](github.com/HannesOberreiter/btree_database).

Our helper tool to create the LLM is Langchain [https://github.com/hwchase17/langchain/](github.com/hwchase17/langchain/).

As AI framework we use [https://openai.com/](openai.com/).

## Structure

- `content` contains the files to upload
- `references_example.json` helper file to reference content files with metadata, needs to be renamed to `references.json`
- `example.env` contains needed API keys and other environment variables, needs to be renamed to `.env`
