## LLM代理

用于构建大型语言模型(LLM)控制代理的小型库,该模型深受<a href="https://github.com/hwchase17/langchain/" target="_blank">langchain</a>的启发.

目的是能够更好地掌握此类代理的工作原理并且能够通过很少的代码来解释它

Langchain很棒,但是它已经有了很多的文件和抽象层,所以我认为从头开始构建一个简单代理的最重要的部分是很棒的.

更多的信息请参见<a href="https://news.ycombinator.com/item?id=35446171">this Hacker News discussion from April 5th 2023</a> 和 <a href="https://www.paepper.com/blog/posts/intelligent-agents-guided-by-llms/">related blog post</a>.

### 如何运行的

代理运行的工作原理如下:

* 它收到提示的指令,告诉它用工具解决任务的基本方法.
* 工具是代理可以使用的自定义构建的组件
    * 到目前为止,我们已经实现了在REPL中执行python代码,使用Google搜索以及在Hacker News上搜索的功能.
* 代理在思想、行动、观察、思想...的循环中进行的.
    * 思想和行动(以及行动的行动输入)是由大语言模型生成的部分
    * T观察是通过使用工具生成的(例如Python的print输出或Google搜索的文本结果)
* LLM在每个循环周期中获取附加到提示的新信息,从而可以根据该信息采取行动
* 一旦代理获得足够多的信息,它就能够提供最终的答案

有关其工作原理的更多详细信息,请查看 <a href="https://www.paepper.com/blog/posts/intelligent-agents-guided-by-llms/">this blog post</a>

### 如何使用

您可以通过在克隆后在其目录中运行以下命令在本地安装: `pip install -e .` 

您还需要提供以下环境变量:

* `OPENAI_API_KEY` 使用OpenAI API (可在以下位置获取: https://platform.openai.com/account/api-keys)
* `SERPAPI_API_KEY` 如果您使用该工具,请使用Google搜索 (可在以下位置获取: https://serpapi.com/)

您可以简单的导出它们,例如: `export OPENAI_API_KEY='sh-lsdf....'`

然后您可以运行脚本 `python run_agent.py` 并提出您的问题:

要构建您自己的代理,请像这样:

```python
from llm_agents import Agent, ChatLLM, PythonREPLTool, HackerNewsSearchTool, SerpAPITool

agent = Agent(llm=ChatLLM(), tools=[PythonREPLTool(), SerpAPITool(), HackerNewsSearchTool()])
result = agent.run("Your question to the agent")

print(f"Final answer is {result}")
```

当然,您也可以构建自定义工具或省略工具,例如,如果您不想创建SERPAPI密钥.
