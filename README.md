
# Description

Agent for Enhancing and Evaluating Ideas - Proof-of-Concept

This project is made for my thesis. The models are LLM based Agent that can evaluate a concept or an idea with given organisational context.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`
`ELSEVIER_API_KEY`
`TAVILY_API_KEY`



## Using the Model

You'll need to install all the dependencies. There might be some that are out of date or not listed, so install them manually.

Model V2 is the final version.

However, the system prompt was modified to not include any information about the company. You'll have to do that yourself.

You also have to add pdf(s) to the pdf.py file if you want to use the tool "PDF report". Otherwise comment out or remove the tool.

Remember to change the tool descriptions to match your context for best possible results.

