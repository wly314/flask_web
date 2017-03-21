# Flask Web 开发层级项目设计
```
Tree结构：
├─.idea
├─Doc
├─Libs
├─venv
└─youmei
    ├─config            存放配置文件
    ├─db_migration      数据库迁移
    ├─forms             Forms
    ├─models            Models
    ├─static            静态文件
    │  ├─css
    │  ├─js
    │  └─libs
    ├─templates         网站模板
    ├─utils             相关工具库
    └─views             视图
```
对应用（youmei）的分层说明：
### config
config里面存放配置文件，包含：公共配置，开发环境配置，产品环境配置，测试环境配置等。
把配置单独拿出来作为一个模块，便于更改。
### db_migration
数据库迁移，其中在```utils```中有一个数据库迁移工具，包含增删改查等操作，在本迁移模块中，只需要调用执行相应的操作就可以。
其中，相应的操作需要自己去写。
