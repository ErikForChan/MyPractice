<%@page import="javax.swing.text.Document"%>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    <link rel="stylesheet" type="text/css" href="<%=path %>/css/head.css"/>
    <title>My JSP 'head.jsp' starting page</title>

  </head>
  
  <body>
    <div class="info">
    <div class="time" align="center"><script> 
    document.write("<span id=time></span>") //输出显示时间日期的容器 
    //每1000毫秒(即1秒) 执行一次本段代码 
    setInterval("time.innerText=new Date().toLocaleString()",1000)  
      </script></div>
    <div class="username"><marquee behivior="alternate">在线用户： <%=request.getAttribute("username") %></marquee scrollAmount=></div>
    <div class="shoppingcar"><a href="shopcarServlet" target="_top">我的购物车</a></div>
    <div class="login"><a href="jsp/login.jsp" target="_top"><input type="button" value="登陆" ></input></a></div>
    <div class="register"><a href="jsp/register.jsp" target="_top"><input type="button" value="注册"></input></a></div>  
    <div class="logout"><a href="logoutServlet" target="_top"><input type="button" value="注销"></input></a></div>  
    </div>
    <form action="fuzzyServlet" method="post" target="right">
        <table align="center" class="inputSearch">
        <tr>
            <td align="right"><input type="text" class="book" name="text"
            value="请输入搜索关键字" onFocus="if(value==defaultValue){value='';this.style.color='#000'}" 
        onBlur="if(!value){value=defaultValue;this.style.color='#999'}" style="color:#999999" /></td>
            <td align="left">            
            <input type="submit" class="search" value="搜索"/>
            </td>
        </tr>
    </table>
    </form>
    
  </body>
</html>
