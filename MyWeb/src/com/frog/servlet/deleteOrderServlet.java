package com.frog.servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.frog.dao.CartDao;
import com.frog.dao.OrderDao;

public class deleteOrderServlet extends HttpServlet {

	
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doPost(request, response);
	}

	
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
    
		 response.setCharacterEncoding("UTF-8");  
         response.setContentType("text/html;charset=utf-8");
         String username=(String) request.getSession().getAttribute("username");
		 String bookname=(String) request.getSession().getAttribute("bookname");
		 new CartDao().cutCart(username);		
		 request.getRequestDispatcher("jsp/ordersuccess.jsp").forward(request, response);
	}

}
