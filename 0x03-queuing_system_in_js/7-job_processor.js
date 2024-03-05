import kue from "kue";

const blacklistPhone = ["4153518780", "4153518781"];

const queue = kue.createQueue();

const sendNotification = function (phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklistPhone.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }
  job.progress(50, 100);
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
  done();
};

queue.process("push_notification_code_2", 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
