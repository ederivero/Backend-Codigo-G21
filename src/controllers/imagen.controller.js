import AWS from "aws-sdk";

export const generarURLFirmada = async (req, res) => {
  const data = req.body;
  const s3 = new AWS.S3();
  // putObject sirve para indicar que la url generada se usara para subir un archivo
  // getObject
  const url = s3.getSignedUrl("putObject", {
    Bucket: process.env.BUCKET_NAME,
    Key: data.nombreArchivo,
    Expires: 60, // El valor es en numeros y representa la cantidad de segundos que sera valido
    // Tipo de Archivo que vamos a subir
    ContentType: data.contentType,
  });

  return res.json({
    content: url,
  });
};
