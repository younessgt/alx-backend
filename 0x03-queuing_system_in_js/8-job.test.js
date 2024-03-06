import { expect } from "chai";
import createPushNotificationsJobs from "./8-job.js";
import kue from "kue";

const queue = kue.createQueue();

describe("test createPushNotificationsJobs", () => {
  before(() => {
    queue.testMode.enter();
  });

  beforeEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it("should throw error if jobs is not an array", () => {
    expect(() => createPushNotificationsJobs(209, queue)).to.throw(
      "Jobs is not an array"
    );
  });

  it("should create a jobs", () => {
    queue.createJob("Job1", { language: "fr" }).save();

    queue.createJob("Job2", { language: "en" }).save();

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].data).to.equal({ language: "fr" });
    expect(queue.testMode.jobs[0].type).to.equal("Job1");

    expect(queue.testMode.jobs[1].data).to.equal({ language: "en" });
    expect(queue.testMode.jobs[1].type).to.equal("Job2");
  });
});
