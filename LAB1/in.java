import java.io.*;
public class in{
	public static void main(String [] args){
		FileReader in=null;
		FileWriter out=null;
		try{
			in=new FileReader("in.txt");
			out=new FileWriter("/home/student/Documents/out.txt");
			int c;
			while((c=in.read())!=-1){
				out.write(c);
			}
		}catch(Exception e){

		}
		finally{
			try{
			if(in!=null) {

				in.close();
				
			}

			if(out!=null)
				{ 
					out.close();
			}}catch(Exception e){
				
			}
		}

	}
}