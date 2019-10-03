import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File; 
import java.io.ByteArrayInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.nio.ByteBuffer; 
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Arrays; 
import java.math.BigInteger;

/*  'proto' homework assignment for Erica Andrews (July 2019)  */

public class HomeworkProto {

    
	public static void main(String[] args ) {
		processFile() ; 
	}
    
    
	public static void processFile() {
		ByteArrayInputStream bain=readFileBytes ();
		byte fheader[]=new byte[10];
		byte fbinaryT[]=new byte[21] ;
		byte firstbyte[]=new byte[1] ;
		int i;
		int numRecords; 
		
		int recordType=6; 
		double amount=0.0f; 
		BigInteger userID; 
		double userAmountTracked=0.0f; 
		double totalDebits=0.0f; 
		double totalCredits=0.0f; 
		int numStartAutopay=0; 
		int numEndAutopay=0; 
		BigInteger userIDtoTrack=new BigInteger("2456938384156277127"); 
		
		if (bain.available()>9) {
			i=bain.read(fheader,0,9); 
		} 
		ByteBuffer bb = ByteBuffer.wrap(Arrays.copyOfRange(fheader, 5, 9));
		numRecords=bb.getInt(); 
		
		while (bain.available()>11) {
			bain.read(firstbyte,0,1); 
			recordType=firstbyte[0];
			
			if (recordType==0 || recordType==1) {
				if (bain.available()>19) {	bain.read(fbinaryT,0,20); }
				userID=new BigInteger(Arrays.copyOfRange(fbinaryT, 4, 12)); 
				//System.out.println("userID : "+userID) ; 

				bb = ByteBuffer.wrap(Arrays.copyOfRange(fbinaryT, 12, 20));
				amount=bb.getDouble(); 
				//System.out.println("amount is : "+amount) ; 
				if (recordType==0) {totalDebits=totalDebits-amount;   }
				else {totalCredits=totalCredits+amount;  }
								
				if (userID.equals(userIDtoTrack)) {
						if (recordType==1) { //credit 
							userAmountTracked=userAmountTracked+amount;
						} else {userAmountTracked=userAmountTracked-amount;} // debit
				}
				

			}
			if (recordType==2 || recordType==3) {
				if (bain.available()>11) {	bain.read(fbinaryT,0,12); }
				
				if (recordType==2 ) {numStartAutopay++;} 
				else {numEndAutopay++;}
			}			
			
		}

	System.out.println("Total records processed: " + numRecords+"\n");	
	System.out.println ("\n\n---------ANSWERS TO QUESTIONS [JAVA VERSION]---------\n\n");
	
	System.out.println ("What is the total amount in dollars of debits?   ANSWER: "+totalDebits+"\n");
	System.out.println ("What is the total amount in dollars of credits?   ANSWER: "+totalCredits+"\n");
	System.out.println ("How many autopays were started?   ANSWER: "+numStartAutopay+"\n");
	System.out.println ("How many autopays were ended?   ANSWER: "+numEndAutopay+"\n");
	System.out.println ("What is balance of user ID 2456938384156277127?   ANSWER: $"+userAmountTracked+"\n");	
		
	}	
	
    public static ByteArrayInputStream readFileBytes ()  {   
    
        String prevFilePath= "txnlog.dat"; 
        return new ByteArrayInputStream(read(prevFilePath) ); 
    

    }
    

    
    /** Read the given binary file, and return its contents as a byte array.*/ 
    private static byte[] read(String aInputFileName){

      File file = new File(aInputFileName);
      //System.out.println("File size: " + file.length());
      byte[] result = new byte[(int)file.length()];
        InputStream input = null;
      try {

        try {
          int totalBytesRead = 0;
          input = new BufferedInputStream(new FileInputStream(file));
          while(totalBytesRead < result.length){
            int bytesRemaining = result.length - totalBytesRead;
            //input.read() returns -1, 0, or more :
            int bytesRead = input.read(result, totalBytesRead, bytesRemaining); 
            if (bytesRead > 0){
              totalBytesRead = totalBytesRead + bytesRead;
            }
          }

        }

      catch (FileNotFoundException ex) {
        System.out.println("File not found: " + "txnlog.dat");
      }
      } catch (IOException ex) {
		System.out.println("An error occurred reading the file: " + "txnlog.dat");
        System.out.println(ex);
      }
       finally {
            System.out.println("Closing file input stream.");
            try {
            
                if (input != null) {input.close(); }
            } catch (Exception ex) {}
         }
      return result;
    }
    

    
}
