package com.frog.dao;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import com.frog.bean.Book;
import com.frog.bean.User;

public class BookDao {

	public BookDao() {
		// TODO Auto-generated constructor stub
	}
	
	public List<Book> fuzzySearch(String fuzzyName) {
		System.out.println("执行0");
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from book where bookname  like '%"+fuzzyName+"%';";
		//like '%'+fuzzyName+'%'
		List<Book> list = new ArrayList<Book>();
		System.out.println("执行前");
		try{
			ps=con.prepareStatement(sql);
			rs=ps.executeQuery();
			while(rs.next()){
				System.out.println("执行ing");
				Book book=new Book();
				book.setBookname(rs.getString(1));
				book.setBooktype(rs.getString(2));
				book.setPrice(rs.getInt(3));
				book.setSales(rs.getInt(4));
				book.setPublishtime(rs.getString(5));
				book.setPublisher(rs.getString(6));
				book.setAuthor(rs.getString(7));
				book.setDescription(rs.getString(8));
				book.setImgURL(rs.getString(9));
				list.add(book);
			}
			System.out.println("执行后");
			return list;
		}catch(Exception e){
			e.printStackTrace();
		}
		try {
			if(rs!=null){rs.close();}
			ps.close();
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
	
	public Book findByBookName(String bookName){
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from book where bookname= ?;";
		Book book=new Book();
		try{
		
			ps=con.prepareStatement(sql);
			ps.setString(1, bookName);
			rs=ps.executeQuery();
			while(rs.next()){
				book.setBookname(rs.getString(1));
				book.setBooktype(rs.getString(2));
				book.setPrice(rs.getInt(3));
				book.setSales(rs.getInt(4));
				book.setPublishtime(rs.getString(5));
				book.setPublisher(rs.getString(6));
				book.setAuthor(rs.getString(7));
				book.setDescription(rs.getString(8));
				book.setImgURL(rs.getString(9));
				return book;
			}
		//	System.out.println(user.getUsername());

		}catch(Exception e){
			e.printStackTrace();
		}
		try {
		 	if(rs!=null)rs.close();
		 	ps.close();
		 	con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}

	public List<Book> findBooks() {
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from book";	
		List<Book> list = new ArrayList<Book>();
		try{
			ps=con.prepareStatement(sql);
			rs=ps.executeQuery();
			while(rs.next()){
			
				Book book=new Book();
				book.setBookname(rs.getString(1));
				book.setBooktype(rs.getString(2));
				book.setPrice(rs.getInt(3));
				book.setSales(rs.getInt(4));
				book.setPublishtime(rs.getString(5));
				book.setPublisher(rs.getString(6));
				book.setAuthor(rs.getString(7));
				book.setDescription(rs.getString(8));
				book.setImgURL(rs.getString(9));
				list.add(book);
			}
			return list;
		}catch(Exception e){
			e.printStackTrace();
		}
		try {
			rs.close();
			ps.close();
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}

	public List<Book> findBooksByType(String bookType) {
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from book where booktype= ?;";	
		System.out.println("执行前");
		List<Book> list = new ArrayList<Book>();
		try{
			ps=con.prepareStatement(sql);
			ps.setString(1, bookType);
			rs=ps.executeQuery();	
			while(rs.next()){	
				System.out.println("执行中");
				Book book=new Book();
				book.setBookname(rs.getString(1));
				book.setBooktype(rs.getString(2));
				book.setPrice(rs.getInt(3));
				book.setSales(rs.getInt(4));
				book.setPublishtime(rs.getString(5));
				book.setPublisher(rs.getString(6));
				book.setAuthor(rs.getString(7));
				book.setDescription(rs.getString(8));
				book.setImgURL(rs.getString(9));
				list.add(book);
			}
			System.out.println("执行后");
			return list;
		}catch(Exception e){
			e.printStackTrace();
		}
		try {
			if(rs!=null){rs.close();}
			
			ps.close();
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
	
	public List<Book> findBooksByPrice(int lowest,int highest) {
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from book where price between ? and ?;";	
		System.out.println("执行前");
		List<Book> list = new ArrayList<Book>();
		try{
			ps=con.prepareStatement(sql);
			ps.setInt(1, lowest);
			ps.setInt(2, highest);
			rs=ps.executeQuery();	
			while(rs.next()){	
				System.out.println("执行中");
				Book book=new Book();
				book.setBookname(rs.getString(1));
				book.setBooktype(rs.getString(2));
				book.setPrice(rs.getInt(3));
				book.setSales(rs.getInt(4));
				book.setPublishtime(rs.getString(5));
				book.setPublisher(rs.getString(6));
				book.setAuthor(rs.getString(7));
				book.setDescription(rs.getString(8));
				book.setImgURL(rs.getString(9));
				list.add(book);
			}
			System.out.println("执行后");
			return list;
		}catch(Exception e){
			e.printStackTrace();
		}
		try {
			if(rs!=null){rs.close();}
			
			ps.close();
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
	
	
	public List<Book> findBooksByLowPrice(int lowest) {
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from book where price< ?;";	
		System.out.println("执行前");
		List<Book> list = new ArrayList<Book>();
		try{
			ps=con.prepareStatement(sql);
			ps.setInt(1, lowest);
			rs=ps.executeQuery();	
			while(rs.next()){	
				System.out.println("执行中");
				Book book=new Book();
				book.setBookname(rs.getString(1));
				book.setBooktype(rs.getString(2));
				book.setPrice(rs.getInt(3));
				book.setSales(rs.getInt(4));
				book.setPublishtime(rs.getString(5));
				book.setPublisher(rs.getString(6));
				book.setAuthor(rs.getString(7));
				book.setDescription(rs.getString(8));
				book.setImgURL(rs.getString(9));
				list.add(book);
			}
			System.out.println("执行后");
			return list;
		}catch(Exception e){
			e.printStackTrace();
		}
		try {
			if(rs!=null){rs.close();}
			
			ps.close();
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}

	
	public List<Book> findBooksByHighPrice(int highest) {
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from book where price> ?;";	
		System.out.println("执行前");
		List<Book> list = new ArrayList<Book>();
		try{
			ps=con.prepareStatement(sql);
			ps.setInt(1, highest);
			rs=ps.executeQuery();	
			while(rs.next()){	
				System.out.println("执行中");
				Book book=new Book();
				book.setBookname(rs.getString(1));
				book.setBooktype(rs.getString(2));
				book.setPrice(rs.getInt(3));
				book.setSales(rs.getInt(4));
				book.setPublishtime(rs.getString(5));
				book.setPublisher(rs.getString(6));
				book.setAuthor(rs.getString(7));
				book.setDescription(rs.getString(8));
				book.setImgURL(rs.getString(9));
				list.add(book);
			}
			System.out.println("执行后");
			return list;
		}catch(Exception e){
			e.printStackTrace();
		}
		try {
			if(rs!=null){rs.close();}
			
			ps.close();
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
	
	public List<Book> findBooksByDate(String begin,String end) {
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from book where publishtime between ? and ?;";	
		System.out.println("执行前");
		List<Book> list = new ArrayList<Book>();
		try{
			ps=con.prepareStatement(sql);
			ps.setString(1, begin);
			ps.setString(2, end);
			rs=ps.executeQuery();	
			while(rs.next()){	
				System.out.println("执行中");
				Book book=new Book();
				book.setBookname(rs.getString(1));
				book.setBooktype(rs.getString(2));
				book.setPrice(rs.getInt(3));
				book.setSales(rs.getInt(4));
				book.setPublishtime(rs.getString(5));
				book.setPublisher(rs.getString(6));
				book.setAuthor(rs.getString(7));
				book.setDescription(rs.getString(8));
				book.setImgURL(rs.getString(9));
				list.add(book);
			}
			System.out.println("执行后");
			return list;
		}catch(Exception e){
			e.printStackTrace();
		}
		try {
			if(rs!=null){rs.close();}
			
			ps.close();
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
	
	public List<Book> findBooksByBefore(String Before) {
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from book where publishtime <= ?;";	
		System.out.println("执行前");
		List<Book> list = new ArrayList<Book>();
		try{
			ps=con.prepareStatement(sql);
			ps.setString(1, Before);
			rs=ps.executeQuery();	
			while(rs.next()){	
				System.out.println("执行中");
				Book book=new Book();
				book.setBookname(rs.getString(1));
				book.setBooktype(rs.getString(2));
				book.setPrice(rs.getInt(3));
				book.setSales(rs.getInt(4));
				book.setPublishtime(rs.getString(5));
				book.setPublisher(rs.getString(6));
				book.setAuthor(rs.getString(7));
				book.setDescription(rs.getString(8));
				book.setImgURL(rs.getString(9));
				list.add(book);
			}
			System.out.println("执行后");
			return list;
		}catch(Exception e){
			e.printStackTrace();
		}
		try {
			if(rs!=null){rs.close();}
			
			ps.close();
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
	
	public List<Book> findBooksByAfter(String After) {
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from book where publishtime >= ?;";	
		System.out.println("执行前");
		List<Book> list = new ArrayList<Book>();
		try{
			ps=con.prepareStatement(sql);
			ps.setString(1, After);
			rs=ps.executeQuery();	
			while(rs.next()){	
				System.out.println("执行中");
				Book book=new Book();
				book.setBookname(rs.getString(1));
				book.setBooktype(rs.getString(2));
				book.setPrice(rs.getInt(3));
				book.setSales(rs.getInt(4));
				book.setPublishtime(rs.getString(5));
				book.setPublisher(rs.getString(6));
				book.setAuthor(rs.getString(7));
				book.setDescription(rs.getString(8));
				book.setImgURL(rs.getString(9));
				list.add(book);
			}
			System.out.println("执行后");
			return list;
		}catch(Exception e){
			e.printStackTrace();
		}
		try {
			if(rs!=null){rs.close();}
			
			ps.close();
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}

}
