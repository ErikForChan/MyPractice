<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@page import="com.frog.dao.*"%>
<%@page import="com.frog.bean.*"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    <link rel="stylesheet" type="text/css" href="<%=path %>/css/myshopcar.css"/>
    <title>My JSP 'myshopcar.jsp' starting page</title>
  

  </head>
  
  <body>
  
    <div class="top">
    
    <div class="info">
    <div class="time"><script style="align:right"> 
    document.write("<span id=time></span>") //输出显示时间日期的容器 
    //每1000毫秒(即1秒) 执行一次本段代码 
    setInterval("time.innerText=new Date().toLocaleString()",1000)  
      </script></div>
    <div class="username"><marquee behivior="alternate">在线用户： <%=request.getAttribute("username") %></marquee scrollAmount=></div>
    <div class="shoppingcar"></div>
    <div class="login"><a href="jsp/login.jsp" target="_top"><input type="button" value="登陆" ></input></a></div>
    <div class="register"><a href="jsp/register.jsp" target="_top"><input type="button" value="注册"></input></a></div>  
    <div class="logout"><a href="logoutServlet" target="_top"><input type="button" value="注销"></input></a></div>  
    </div>
   
    <div class="washu">
    	<a href="index.jsp"><div class="logo"></div></a>
    	<div class="myshopcar"></div>
    </div>
    </div>
    
    <hr style="background-color:#8fd6f5;height:3px;">
    
    <center>
         <table cellpadding="1"  style="border-style:dashed; border-width:1px; border-color:#00a0e9;" width="1200px" >
         <tr align="center" width="1200px">
                <td height="30px" class="book">图书</td>
                <td height="30px" class="book">书名</td>
                <td height="30px" class="book">单价</td>
                <td height="30px" class="book">数量</td>
                <td height="30px" class="book">总价</td>
                <td height="30px" class="book">操作</td>
         </tr>  
         <%
             List<Cart> list=(List<Cart>)request.getAttribute("AllKindCart");
             Iterator<Cart> it=null;
             if(list==null){System.out.println("list为空");}
             request.getSession().setAttribute("AllCart", list);
             
             if(list!=null){
             it=list.iterator();
             }
             Cart cart=null;
             while(it.hasNext()){
                 cart=it.next();
                 request.getSession().setAttribute("username",cart.getUsername());           
                 request.getSession().setAttribute("bookname",cart.getBookname());      
             %>
              <tr align="center" width="1200px">
                <td width="100px" height="120px"><img class="bookimage" alt="图书" src=<%=cart.getImgURL() %> ></td>
                <td width="100px" height="120px" class="book"><%=cart.getBookname() %></td>
                <td width="100px" height="120px" class="book"><%=cart.getPrice() %></td>
                <td width="100px" height="120px" class="book" align="center"><a href="cutCountServlet?username=<%=cart.getUsername() %>&bookname=<%=cart.getBookname() %>"><img alt="" src="images/cut.png"></a>    <%=cart.getCount() %>    <a href="addCountServlet?username=<%=cart.getUsername() %>&bookname=<%=cart.getBookname() %>"><img alt="" src="images/add.png"></a></td>      
                <td width="100px" height="120px" class="book"><%=cart.getTotalprice() %></td>
                <td width="100px" height="120px">
                <div class="delete"><a href="deleteCartServlet?username=<%=cart.getUsername() %>&bookname=<%=cart.getBookname() %>"><img alt="" src="images/delete.png"></a></div></td>
              </tr>   
                     
            <%
              }       
            %>     
            
            </table>
          
        </center>
        
        <div class="cash"><a href="addOrder"><img alt="" src="images/cash.png"></a></div>

  </body>
</html>
