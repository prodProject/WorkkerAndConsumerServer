cd protos
echo [COMPILEING..........]
protoc address.proto --python_out=..\protobuff
protoc date.proto --python_out=..\protobuff
protoc email.proto --python_out=..\protobuff
protoc mobile.proto --python_out=..\protobuff
protoc contactdetails.proto --python_out=..\protobuff
protoc entity.proto --python_out=..\protobuff
protoc names.proto --python_out=..\protobuff
protoc gender.proto --python_out=..\protobuff
protoc uid.proto --python_out=..\protobuff
protoc worker.proto --python_out=..\protobuff
protoc workertype.proto --python_out=..\protobuff

cd ..
