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

public class addOrder extends HttpServlet {

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
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
        boolean flag=false;
        while(it.hasNext()){
            cart=it.next();                       
  	        Connection con=null;
  	        PreparedStatement pst=null;
  	        Date date=new Date();
  	        DateFormat format=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
  	        String time=format.format(date);
  	        System.out.println("执行前");
  	        try{
  	        con=JdbcUtil.getConnection();
  	        con.setAutoCommit(false);		    
  	        String sql="insert into orders values (?,?,?,?,?,?,?,?)";
  	        pst=con.prepareStatement(sql);
  			pst.setString(1, cart.getBookname());
  			System.out.println(cart.getBookname());
  			pst.setString(2, time);
  			pst.setInt(3, cart.getPrice());
  			pst.setInt(4, cart.getCount());
  			pst.setInt(5, cart.getTotalprice());
  			pst.setString(6, user.getUsername());
			pst.setString(7, user.getAddress());
			pst.setString(8, user.getPhone());
  			pst.executeUpdate();
  			System.out.println("执行后");
  			con.commit();
			   flag=true;
			   pst.close();
			   con.close();
			}catch(Exception e){
			e.printStackTrace();
			} 
  	       
  	      
        }
        PrintWriter out=response.getWriter();	
        if(flag){
	    	   
	            request.getRequestDispatcher("myorderSelvlet").forward(request,response);          
	                 
	        }else{
	                  out.print("加入订单失败!");
	       }
	       
	}


	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doGet(request,response);   
	}

}
