const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    if (!path) {
      reject(new Error('Cannot load the database'));
      return;
    }

    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split(/\r?\n/).filter((line) => line.trim() !== '');

      if (lines.length === 0) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const students = lines.slice(1);
      const output = [];

      const totalMsg = `Number of students: ${students.length}`;
      console.log(totalMsg);
      output.push(totalMsg);

      const fields = {};
      students.forEach((student) => {
        const parts = student.split(',');
        if (parts.length >= 4) {
          const firstname = parts[0].trim();
          const field = parts[3].trim();
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        }
      });

      for (const [field, names] of Object.entries(fields)) {
        const fieldMsg = `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
        console.log(fieldMsg);
        output.push(fieldMsg);
      }

      resolve(output.join('\n'));
    });
  });
}

module.exports = countStudents;
