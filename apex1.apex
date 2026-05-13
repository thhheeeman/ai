public class First {

    public static void sendMail(String address, String subject, String body) {

        Messaging.SingleEmailMessage mail =
            new Messaging.SingleEmailMessage();

        String[] toAddresses = new String[] {address};

        mail.setToAddresses(toAddresses);

        mail.setSubject(subject);

        mail.setPlainTextBody(body);

        Messaging.sendEmail(
            new Messaging.SingleEmailMessage[] { mail }
        );
    }
}






string address = 'atharvamahulkar12@gmail.com';
string subject = 'Speaker Confirmation';
String body = 'Thank you for speaking at the conference.';
first.sendMail(address, subject, body);
