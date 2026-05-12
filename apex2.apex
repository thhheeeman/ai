public class StudentManager {

    // Variables
    String studentName;
    Integer marks;

    // Constructor
    public StudentManager(String name, Integer m) {

        studentName = name;
        marks = m;
    }

    // Method
    public void displayResult() {

        System.debug('Student Name: ' + studentName);
        System.debug('Marks: ' + marks);

        // If Else
        if(marks >= 40) {

            System.debug('Result: PASS');

        } else {

            System.debug('Result: FAIL');
        }
    }

    // Main Method
    public static void mainMethod() {

        // List
        List<StudentManager> students =
            new List<StudentManager>();

       students.add(
            new StudentManager('def', 85)
        );

        students.add(
            new StudentManager('abc', 30)
        );

    
        for(StudentManager s : students) {

            s.displayResult();
            System.debug('----------------');
        }
    }
}
