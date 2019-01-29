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

public class fuzzyServlet extends HttpServlet {

	
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		doPost(request,response);
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		request.setCharacterEncoding("UTF-8");
		String fuzzyName=request.getParameter("text");
		//String word="JQuery";
		List<Book> list=new BookDao().fuzzySearch(fuzzyName);
		System.out.println(fuzzyName);
		request.setAttribute("AllKindBook", list);
		request.getRequestDispatcher("jsp/showbook.jsp").forward(request, response);
	}

}
