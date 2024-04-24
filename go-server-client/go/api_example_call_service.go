// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

/*
 * Example API
 *
 * Example API spec
 *
 * API version: v1
 * Contact: example@example-team.com
 */

package openapi

import (
	"context"
	"net/http"
	"errors"
)

// ExampleCallAPIService is a service that implements the logic for the ExampleCallAPIServicer
// This service should implement the business logic for every endpoint for the ExampleCallAPI API.
// Include any external packages or services that will be required by this service.
type ExampleCallAPIService struct {
}

// NewExampleCallAPIService creates a default api service
func NewExampleCallAPIService() ExampleCallAPIServicer {
	return &ExampleCallAPIService{}
}

// GetChildrenByExampleParentId - Get children of parent by example parent ID.
func (s *ExampleCallAPIService) GetChildrenByExampleParentId(ctx context.Context, id string, limit int32) (ImplResponse, error) {
	// TODO - update GetChildrenByExampleParentId with the required logic for this service method.
	// Add api_example_call_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, GetChildrenByExampleParentId200Response{}) or use other options such as http.Ok ...
	// return Response(200, GetChildrenByExampleParentId200Response{}), nil

	// TODO: Uncomment the next line to return response Response(401, interface{}{}) or use other options such as http.Ok ...
	// return Response(401, interface{}{}), nil

	// TODO: Uncomment the next line to return response Response(500, GetChildrenByExampleParentId500Response{}) or use other options such as http.Ok ...
	// return Response(500, GetChildrenByExampleParentId500Response{}), nil

	return Response(http.StatusNotImplemented, nil), errors.New("GetChildrenByExampleParentId method not implemented")
}

// GetExampleParentById - Get example parent by ID.
func (s *ExampleCallAPIService) GetExampleParentById(ctx context.Context, id string, limit int32) (ImplResponse, error) {
	// TODO - update GetExampleParentById with the required logic for this service method.
	// Add api_example_call_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, GetExamples200Response{}) or use other options such as http.Ok ...
	// return Response(200, GetExamples200Response{}), nil

	// TODO: Uncomment the next line to return response Response(401, interface{}{}) or use other options such as http.Ok ...
	// return Response(401, interface{}{}), nil

	// TODO: Uncomment the next line to return response Response(500, GetExampleParentById500Response{}) or use other options such as http.Ok ...
	// return Response(500, GetExampleParentById500Response{}), nil

	return Response(http.StatusNotImplemented, nil), errors.New("GetExampleParentById method not implemented")
}

// GetExamples - Get examples.
func (s *ExampleCallAPIService) GetExamples(ctx context.Context, limit int32) (ImplResponse, error) {
	// TODO - update GetExamples with the required logic for this service method.
	// Add api_example_call_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, GetExamples200Response{}) or use other options such as http.Ok ...
	// return Response(200, GetExamples200Response{}), nil

	// TODO: Uncomment the next line to return response Response(401, interface{}{}) or use other options such as http.Ok ...
	// return Response(401, interface{}{}), nil

	// TODO: Uncomment the next line to return response Response(500, GetExamples500Response{}) or use other options such as http.Ok ...
	// return Response(500, GetExamples500Response{}), nil

	return Response(http.StatusNotImplemented, nil), errors.New("GetExamples method not implemented")
}
