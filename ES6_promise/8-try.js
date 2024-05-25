export default function divideFunction(numerator, denominator) {
  return new Promise((resolve, reject) => {
    if (denominator === 0) {
      reject('cannot divide by 0.');
    }
    resolve(numerator / denominator);
  });
}
