package com.frog.servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.frog.bean.Book;
import com.frog.dao.BookDao;

public class lowServlet extends HttpServlet {

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doPost(request,response);
	}

	
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		int lowest=15;
		List<Book> list=new BookDao().findBooksByLowPrice(lowest);
		request.setAttribute("AllKindBook", list);
		request.getRequestDispatcher("jsp/showbook.jsp").forward(request, response);
	}

}
