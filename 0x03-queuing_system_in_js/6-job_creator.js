import kue from "kue";

const queue = kue.createQueue();

const obj = {
  phoneNumber: "01234567898",
  message: "Hello Alx",
};

const job = queue.create("push_notification_code", obj).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on("complete", () => console.log("Notification job completed"));
job.on("failed", () => console.log("Notification job failed"));
