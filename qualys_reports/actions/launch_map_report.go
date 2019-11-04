package actions

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// LaunchMapReportInputOutputFormatPdf is an enumerated value
const LaunchMapReportInputOutputFormatPdf = "pdf"

// LaunchMapReportInputOutputFormatHTML is an enumerated value
const LaunchMapReportInputOutputFormatHTML = "html"

// LaunchMapReportInputOutputFormatMht is an enumerated value
const LaunchMapReportInputOutputFormatMht = "mht"

// LaunchMapReportInputOutputFormatXML is an enumerated value
const LaunchMapReportInputOutputFormatXML = "xml"

// LaunchMapReportInputOutputFormatCsv is an enumerated value
const LaunchMapReportInputOutputFormatCsv = "csv"

// LaunchMapReportInput is the input for LaunchMapReport
type LaunchMapReportInput struct {
	Domain        string `json:"domain"`
	IPRestriction string `json:"ip_restriction"`
	OutputFormat  string `json:"output_format"`
	ReportRefs    string `json:"report_refs"`
	TemplateID    int    `json:"template_id"`
	Title         string `json:"title"`
}

// LaunchMapReportOutput is the output for LaunchMapReport
type LaunchMapReportOutput struct {
	ID int `json:"id"`
}

// LaunchMapReportAction is an action the plugin can take
type LaunchMapReportAction struct{}