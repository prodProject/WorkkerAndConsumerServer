cd protos
echo [COMPILEING..........]
protoc deviceinfo.proto --python_out=..\protobuff
protoc address.proto --python_out=..\protobuff
protoc persontypeenum.proto --python_out=..\protobuff
protoc summary.proto --python_out=..\protobuff
protoc time.proto --python_out=..\protobuff
protoc email.proto --python_out=..\protobuff
protoc mobile.proto --python_out=..\protobuff
protoc contactdetails.proto --python_out=..\protobuff
protoc entity.proto --python_out=..\protobuff
protoc names.proto --python_out=..\protobuff
protoc gender.proto --python_out=..\protobuff
protoc uid.proto --python_out=..\protobuff
protoc worker.proto --python_out=..\protobuff
protoc workertype.proto --python_out=..\protobuff
protoc login.proto --python_out=..\protobuff
protoc workersearch.proto --python_out=..\protobuff
protoc consumer.proto --python_out=..\protobuff
protoc registration.proto --python_out=..\protobuff
protoc task.proto --python_out=..\protobuff
cd ..
