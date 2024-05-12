export default function* createIteratorObject(report) {
  for (const department in report) {
    if (Object.prototype.hasOwnProperty.call(report, department)) {
      const employees = report[department];
      for (const employee of employees) {
        yield employee;
      }
    }
  }
}
