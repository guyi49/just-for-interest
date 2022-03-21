


1. 配置中心用的是Nacos；
    - Nacos 放的是配置文件
        - db数据库地址
        
        - redis地址
        - mybatis 指定的xml地址
        - xxxjob
        - 常用文件 
            - 在实现类中使用 @RefreshScope 自动刷新配置
            
    - SBA
 2. rocket mq
 3. K8S

数据库指定不同的schema
    1. 分库完成，通过配置文件
    2. 多数据源的配置需要在代码层实现；
        - config 配置类去实现
        
git config --global user.email "yygu@homeinns.com"       
ssh-keygen -t rsa -C "yygu@homeinns.com"  -f ~/.ssh/id_rsa_company   //上面的邮箱地址
  
# self(182xxxx8804@163.com)
Host github.com    
    Port 22
    User guyi49
    HostName github.com   #github地址
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/id_rsa
# company()
Host 172.23.101.175
    Port 22
    User yygu@homeinn.com
    HostName http://172.23.101.175  #公司gitlab地址
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/id_rsa_company
