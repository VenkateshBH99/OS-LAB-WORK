import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.*;

class RW1{
    static Lock lockR=new ReentrantLock();
    static Lock lockW=new ReentrantLock();
    static Condition canRead=lockR.newCondition();
    static Condition canWrite=lockW.newCondition();
    static int readCount = 0;
    static int NReaders=0;
    static int WaitingReaders=0;
    static int NWriters=0;
    static int WaitingWriters=0;

    static class Read implements Runnable {
        @Override
        public void run() {
            try {
                //Acquire Section

                BeginRead();
                EndRead();
                
               

                //Reading section
                
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
        public static void BeginRead(){
            try{
            if (NWriters == 1 || WaitingWriters > 0) { 
                lockW.lock();
                lockR.lock();
  
                    ++WaitingReaders; 
                System.out.println("Thread "+Thread.currentThread().getName() + " is READING");
  
                  // Otherwise, a reader waits (maybe many do) 
                       canRead.await(); 
  
                   --WaitingReaders; 
                      } 
  
                    ++NReaders; 
                    canRead.signal();
                    lockR.unlock();
                }catch(Exception e) {
                System.out.println(e.getMessage());
            }

        }
        public static void EndRead(){
            try{
            if(--NReaders==0){
                System.out.println("Thread "+Thread.currentThread().getName() + " has FINISHED READING");

                canWrite.signal();
                lockW.unlock();
            }
        }catch(Exception e) {
                System.out.println(e.getMessage());
            }
        }
    }

    static class Write implements Runnable {
        @Override
        public void run() {
            try {
                BeginWrite();
                EndWrite();
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
        public static void BeginWrite(){
            try{
            if (NWriters == 1 || NReaders > 0) { 
                lockW.lock();
                    ++WaitingWriters; 
                    System.out.println("Thread "+Thread.currentThread().getName() + " is WRITING");
                    canWrite.await();
                    --WaitingWriters; 
                  } 
  
                NWriters = 1;
            }catch(Exception e) {
                System.out.println(e.getMessage());
            }
        }
        public static void EndWrite(){
            try{
            NWriters = 0; 
  
                // Checks to see if any readers are waiting 
               System.out.println("Thread "+Thread.currentThread().getName() + " has finished WRITING");

                if (WaitingReaders>0){
                    canRead.signal();
                    lockR.unlock();
                }
                else{
                    canWrite.signal();
                    lockW.unlock();
                }
            }catch(Exception e) {
                System.out.println(e.getMessage());
            }

        }
    }

    public static void main(String[] args) throws Exception {
        Read read = new Read();
        Write write = new Write();
        Thread t1 = new Thread(read);
        t1.setName("thread1");
        Thread t2 = new Thread(read);
        t2.setName("thread2");
        Thread t3 = new Thread(write);
        t3.setName("thread3");
        Thread t4 = new Thread(read);
        t4.setName("thread4");
        Thread t5=new Thread(write);
        t5.setName("thread5");
        
        t1.start();
        t3.start();
        t2.start();
        t4.start();
        t5.start();
    }
}