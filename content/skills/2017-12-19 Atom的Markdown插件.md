Title: Atom的Markdown Writer插件
Tags: Atom, Markdown

>[markdown-writer](https://atom.io/packages/markdown-writer)插件用于帮助快速编写Markdown文件
>[tool-bar-markdown-writer](https://atom.io/packages/tool-bar-markdown-writer)插件用于将markdown-writer的功能集成到工具条上

### Atom内置
Atom已经内置了很多Snippet用来快速编写Markdown文件, 比如  
- 输入`img`再敲入`tab`键就会快速输入`![]()`
- 输入`table`再敲入`tab`键就会得到一个表格模板
- 输入`b`再敲入`tab`键就会快速输入加粗标记`****`
- 输入`i`再敲入`tab`键就会快速输入斜体标记`**`
- 输入`code`再敲入`tab`键就会快速输入代码块
- ......

### [markdown-writer](https://atom.io/packages/markdown-writer)
但是毕竟这些功能有限, 比如在导入图片的时候还是需要进行很多手工的操作，所以这时候就需要用到[markdown-writer](https://atom.io/packages/markdown-writer)了。  
[markdown-writer](https://atom.io/packages/markdown-writer)的主要有以下这些便捷方式能够方便流畅的写文章:  

##### 快捷键
    "shift-ctrl-I": "markdown-writer:insert-image"              //插入图片
    "shift-ctrl-k": "markdown-writer:insert-link"               //插入链接
    "ctrl-i":       "markdown-writer:toggle-italic-text"        //插入斜体
    "ctrl-b":       "markdown-writer:toggle-bold-text"          //插入粗体
    "ctrl-'":       "markdown-writer:toggle-code-text"          //插入代码文本
    "ctrl-`":       "markdown-writer:toggle-codeblock-text"     //插入代码段  
    "ctrl-h":       "markdown-writer:toggle-strikethrough-text" //插入删除线   
    "ctrl-1":       "markdown-writer:toggle-h1"                 //插入1号标题
    "ctrl-2":       "markdown-writer:toggle-h2"                 //插入2号标题
    "ctrl-3":       "markdown-writer:toggle-h3"                 //插入3号标题
    "ctrl-4":       "markdown-writer:toggle-h4"                 //插入4号标题
    "ctrl-5":       "markdown-writer:toggle-h5"                 //插入5号标题

##### 其他命令
_除了默认已经定义快捷键的命令，还有其他一些命令可以使用，如果使用频繁的话也可以单独设置快捷键_

    markdown-writer:new-draft                           //新建草稿
    markdown-writer:new-post                            //新建文章
    markdown-writer:publish-draft                       //发布草稿
    markdown-writer:toggle-task                         //插入代办事项
    markdown-writer:toggle-taskdone                     //完成代办事项
    markdown-writer:toggle-blockquote                   //插入区块
    markdown-writer:correct-order-list-numbers          //格式化列表
    markdown-writer:insert-table                        //插入表格
    markdown-writer:format-table                        //格式化表格
    markdown-writer:jump-to-next-table-cell             //跳到表格的下一个单元
    markdown-writer:jump-to-next-heading                //跳到下一个标题
    markdown-writer:jump-to-previous-heading            //跳到前一个标题
    markdown-writer:jump-to-reference-definition        //跳到相关定义
    markdown-writer:toggle-task                         //插入代办事项


### [tool-bar-markdown-writer](https://atom.io/packages/tool-bar-markdown-writer)
当然如果你还装了[tool-bar-markdown-writer](https://atom.io/packages/tool-bar-markdown-writer)的话，就吧上面的统统忘了吧，直接用工具条快乐的去写你的文章就行了。  
不过下面的操作方式的了解一下

    shift + New Post: 新建一个草稿(默认是直新建文章的)
    shift + Code: 插入代码段（默认是插入代码句）
    shift + Ordered List: 格式化列表，会读已编辑好的列表进行排序
    shift + Task List: 设置代办事项为完成或者没完成
