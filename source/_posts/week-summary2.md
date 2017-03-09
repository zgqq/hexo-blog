---
title: week-summary2
date: 2017-03-09 19:17:54
tags:
---

# 第一天
## docker
感觉最近要做的工作就是维护+开发了，所以我选择docker， 不过docker在国内的网速真的感人，连翻墙都没有什么卵用，经常出现Connection reset by peer， 解决的办法就是注册国内镜像
https://www.daocloud.io/ ，今天的主要任务就是做一个增删改查，管理敏感词，很简单。docker真的是爽，安装redis,mysql 一条命令搞定，docker里面有一个很重要的关键词volume，这个关键词表示image的某个位置是可挂载的

    docker run --name redis -d --restart=always --publish 6380:6379 --volume /srv/docker     /redis3:/data redis:3.0 --requirepass zgqq

## 命名
另外一个就是命名问题，有很多同类对象的时候，通常有两种命令方式

    String name = "";
    String name2 = "";

另外一种就是
    
    String name1 = "";
    String name2 = "";

我已经做出艰难的选择，选择第二种
# 第二天
# 测试
继续那个敏感词的增删改查，虽然这个没有什么坑，但是项目里面有些代码还是让我难受，代码也没有什么规范，测试也没写，不知道他们一天要测试多少次。写了一个测试类，可以用来模拟http请求

    @RunWith(SpringJUnit4ClassRunner.class)
    @ContextConfiguration({"file:src/main/webapp/WEB-INF/spring/applicationContext.xml"
            , "file:src/main/webapp/WEB-INF/spring/appServlet/servlet-context.xml"})
    @WebAppConfiguration
    public abstract class WebTests {
        @Autowired
        protected WebApplicationContext wac;
        protected MockMvc mockMvc;
    
        @Before
        public void setup() {
            mockMvc = MockMvcBuilders.webAppContextSetup(wac)
                    .defaultRequest(get("/")).build();
        }
    }

断言使用 hamcrest 的assertThat，十分好用，写完测试后
## 文档
接下来就是写文档了，傻傻的我居然用了为知笔记内置的编辑器，用起来贼难受，点着点着突然看到.md后缀的文件，心里暗爽了一下，我要被解救了。因为项目是前后端完全分离，所以我写文档的时候经常需要格式化json，突然想起一个神器jq

    echo '{
    "data":
        {"page_num":1, "page_size": 10}}'|jq

用markdown写完文档后，无聊看了一下坚果云用了多少流量，居然一天用了600m，赶紧查看一下哪个坑爹目录，原来是项目build 后的zip，rar包，添加下忽略规则就好了。
## 新任务
又有新任务了，要搭一个springboot + mybatis + redis + kafka 的模板项目, 主要 kafka 实在太虐人了，docker搭不成功，最后实在没有办法，本地安装后，找了一个官方的sample，不过这个sample已经被更新到spring boot2.0了，想了一招，那就是git reset --hard 回退到以前的版本，参考了下才搞出来
# 第三天
## 数据库
老大要求mybatis需要连接多个数据库,大概就是dao要连接不同的数据库，多数据源我还真没配过，感觉应该不难，最后还是折腾了很久，主要遇到了两个坑，第一个就是mybatis 官方提供的starter，简直就是个坑，它会自动配置mapper，看注释好像只要有ScanMapper，它就不会扫描了，我创建MapperScannerConfigurer，可惜那个starter还是自动扫描，最后把starter给干掉，自已重新配置

    private MapperScannerConfigurer createMapperConfigurer(String basePackage, String sqlSessionFactoryName) {
        MapperScannerConfigurer configurer = new MapperScannerConfigurer();
        configurer.setBasePackage(basePackage);
        configurer.setAnnotationClass(Mapper.class);
        configurer.setSqlSessionFactoryBeanName(sqlSessionFactoryName);
        return configurer;
    }

另外一个坑就是注解bean的依赖关系，同一个@Configuration 内，如果有两个类型相同的bean，
有一个bean 依赖这两个bean其中的一个，你必须设置其中一个为@Primary，否则就会报错
## spring 坑
## 依赖管理
最好不要使用springboot 提供的依赖管理 "io.spring.dependency-management" 

### 自动注入
 另外一个就是，如果一个bean的构造方法传入参数，spring 不会报错，而是自动注入，所以如果有需要的参数的构造方法，最好检查一下field 有没有被@Resources或@Autowired注解，下面是一个典型的错误

    @Autowired
	private final StringRedisTemplate stringRedisTemplate;
    @Autowired
    private final StringRedisTemplate secondaryRedisTemplate;

    public YuntuService(YuntuRepository repository, Yuntu2Repository yuntu2Repository,
                        @Qualifier("primaryStringRedisTemplate")StringRedisTemplate stringRedisTemplate,
                        @Qualifier("secondaryStringRedisTemplate") StringRedisTemplate secondaryRedisTemplate)

