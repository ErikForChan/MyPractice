package com.frog.servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Iterator;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.frog.bean.Cart;
import com.frog.bean.User;
import com.frog.dao.JdbcUtil;
import com.frog.dao.UserDao;

public class usercartservlet extends HttpServlet {

	
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doPost(request,response);
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		List<Cart> list=(List<Cart>) request.getSession().getAttribute("AllCart");
		HttpSession session=request.getSession();
		String username=(String) session.getAttribute("username");
		System.out.println(username);
		User user=new UserDao().findByUserName(username);
		Iterator<Cart> it=null;
        if(list==null){System.out.println("list为空");}
        request.getSession().setAttribute("AllCart", list);
        
        if(list!=null){
        it=list.iterator();
        }
        Cart cart=null;
        while(it.hasNext()){
            cart=it.next();             
            boolean flag=false;
  	        Connection con=null;
  	        PreparedStatement pst=null;
  	        Date date=new Date();
  	        DateFormat format=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
  	        String time=format.format(date);
  	        try{
  	        System.out.println("111");
  	        con=JdbcUtil.getConnection();
  	        con.setAutoCommit(false);		    
  	        String sql="insert into order(bookname,ordertime,price,count,totalprice,username,address,phone) value(?,?,?,?,?,?,?,?);";
  			pst=con.prepareStatement(sql);
  			pst.setString(1, cart.getBookname());
  			pst.setString(2, time);
  			pst.setInt(3, cart.getPrice());
  			pst.setInt(4, cart.getCount());
  			pst.setInt(5, cart.getTotalprice());
  			pst.setString(6, user.getUsername());
  			pst.setString(6, user.getAddress());
  			pst.setString(6, user.getPhone());
  			pst.executeUpdate();
  		}catch(Exception e){
  			e.printStackTrace();
  		}
  		try {
  			pst.close();
  			con.close();
  		} catch (SQLException e) {
  			// TODO Auto-generated catch block
  			e.printStackTrace();
  		}
  	        PrintWriter out=response.getWriter();	
  	       if(flag){
  	    	     out.print("添加订单成功");
  	             // request.getRequestDispatcher("jsp/myorder.jsp").forward(request,response);          
  	                 
  	        }else{
  	                  out.print("加入订单失败!");
  	             }
        }
        } 
       
}
