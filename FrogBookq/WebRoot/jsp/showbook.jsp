<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ page language="java" import="com.frog.bean.Book" %>
<%@page import="java.sql.*"%>
<%@page import="javax.naming.*"%>
<%@page import="javax.activation.DataSource"%>
<%@page import="com.frog.dao.*"%>
<%@page import="com.frog.bean.*"%>
<%@ page language="java" import="com.frog.bean.User" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    <link rel="stylesheet" type="text/css" href="<%=path %>/css/showbook.css"/>
    <title>My JSP 'showbook.jsp' starting page</title>
    

  </head>
  
  <body>
    <center>
    
            <%--<c:forEach var="p" items="${AllKindBook}">
                    <div id="displaybook"> 
                    <div id="bookimage"><img alt="" src="images/BookImages/6.png" ></div>
                    <div id="bookinfo">
                          <table cellpadding="1"  border="0" width="250">
                         
                          <tr height="20"> <div id="" align="left"><c:out value="${p.bookname}"></c:out></div></tr><br/>
                          <tr height="20"> <div id="" align="left">类型：<c:out value="${p.booktype}"></c:out></div></tr><br/>
                          <tr height="20"> <div id="" align="left">价格：<c:out value="${p.price}"></c:out></div></tr><br/>
                          <tr height="20"> <div id="" align="left">销量：<c:out value="${p.sales}"></c:out></div></tr><br/>
                          <tr height="20"> <div id="" align="left">出版日期：<c:out value="${p.publishtime}"></c:out></div></tr><br/>
                          <tr height="20"> <div id="" align="left">出版社：<c:out value="${p.publisher}"></c:out></div></tr><br/>
                          <tr height="20"> <div id="" align="left">作者：<c:out value="${p.author}"></c:out></div></tr><br/>
                          <tr height="40"> <div id="" align="left">详情：<c:out value="${p.description}"></c:out></div></tr><br/>
                          <tr height="30"> <div id="purchase"><a href=""><input type="button" value="加入购物车"></input></a></div></tr>
                          </table>
                    </div>
                    </div>
  
      				<hr style="border:1px dashed #8fd6f5;">
                
                
                </c:forEach> --%>                        
                
             <%
             List<Book> list=(List<Book>)request.getAttribute("AllKindBook");
             Iterator<Book> it=list.iterator();
             Book book=null;
             while(it.hasNext()){
                 book=it.next();            
             %>
               <div id="displaybook"> 
                    <div id="bookimage" ><img alt="图书" src=<%=book.getImgURL() %> ></div>
                    <div id="bookinfo">
                   <table cellpadding="1"  border="0" width="250">      
                   <tr height="20"><div id="" align="left" name=""><%=book.getBookname() %></div></tr><br/> 
                   <tr height="20"><div id="" align="left" name="booktype">类型：<%=book.getBooktype() %></div></tr><br/>
                   <tr height="20"><div id="" align="left" name="">价格：<%=book.getPrice() %></div></tr><br/>
                   <tr height="20"><div id="" align="left" name="sales">销量：<%=book.getSales() %></div></tr><br/>
                   <tr height="20"><div id="" align="left" name="publishtime">出版日期：<%=book.getPublishtime() %></div></tr><br/>
                   <tr height="20"><div id="" align="left" name="publish">出版社：<%=book.getPublisher() %></div></tr><br/> 
                   <tr height="20"><div id="" align="left" name="author">作者：<%=book.getAuthor() %></div></tr><br/> 
                   <tr height="40"><div id="" align="left" name="description">详情：<%=book.getDescription() %></div></tr> <br/> 
                    <%                                        
                     request.getSession().setAttribute("book",book);                            
                    %>   
                       
                   <tr height="30"><div id="purchase">
                   <a href="addCart?bookname=<%=book.getBookname()%>&imageurl=<%=book.getImgURL()%>&price=<%=book.getPrice() %>"> 
                   <img alt="" src="images/addtocart.png">
                   </a></div></tr>
                   
                   </table>
                    </div>
                    </div>
                  
      				<hr style="border:1px dashed #8fd6f5;">
         
            <%
              }       
            %>     

        </center>
  </body>
</html>
