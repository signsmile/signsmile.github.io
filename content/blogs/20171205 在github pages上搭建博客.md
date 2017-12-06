Title: 在github pages上搭建博客
Category: Blogs
Date: 2017-12-05

>在上传Pelican生成的静态网站的时候发现绑定的域名没法访问，
上网一搜是因为缺少CNAME文件的配置，于是决定罗列下github上搭建博客的步骤，以备查询

1. 首先得有个github账号，账号申请就不说了，[github传送门](https://github.com/)

2. 注册账号后[新建一个仓库(repository)](https://github.com/new)  
这里需要特别留意的是仓库的名字必须以`{username}.github.io`命名，`{username}`用自己github的账户名替换  
![新建仓库]({filename}/images/new_github_pages_repository.png)  

3. github上的仓库创建好以后同时也需要在本地创建个仓库以便维护，github会提供操作方法，命令行上照做即可。
>     echo "# signsmile.github.io" >> README.md
>     git init
>     git add README.md
>     git commit -m "first commit"
>     git remote add origin > https://github.com/signsmile/signsmile.github.io.git
>     git push -u origin master

    这里需要事先设置好[ssh公钥私钥]({filename}/blogs/20171204 利用Putty生成SSH公钥私钥.md)，以便获得push的权限。当然也可以在每次push的时候输入账户密码
>     $ git push -u origin master
>     Username for 'https://github.com': signsmile

    ![登录]({filename}/images/github_login.png)

4. 有了仓库以后就可以把整个静态网站放到仓库中去了，比如用Pelican生成的output目录就可以直接上传上去，在这里作为例子，新建一个index.html文件
>     <html>
>         <head>
>             <title>github pages test</title>
>         </head>
>         <body>
>             <h1>Hello World!</h1>
>             this is the test index.html file for github pages
>         </body>
>     </html>

    把index.html文件放在本地仓库，然后`git push`上传到github，这样github pages就可以访问了  
    访问地址为[{username}.github.io](https://signsmile.github.io)  
    ![页面效果]({filename}/images/github_pages_helloworld.png)

5. 如果手头有个域名，可以将自己的域名指向github pages, 配置如下  
    ![域名设置]({filename}/images/github_pages_domain_name_setting.png)  
    同时github仓库的根目录下需要放一个`CNAME`文件，文件内填入将设置的域名，比如`blog.signsmile.com`

至此，github pages上的blog已经搭建完成了，后续只需将更新的静态网站放到仓库目录下面然后`push`就行
