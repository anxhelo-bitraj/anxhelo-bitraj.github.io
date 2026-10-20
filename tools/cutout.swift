import Vision
import CoreImage
import Foundation

// Lift the subject out of a photo (same feature as long-pressing a photo on iPhone) and save it with a transparent background.
let input = URL(fileURLWithPath: CommandLine.arguments[1])
let output = URL(fileURLWithPath: CommandLine.arguments[2])
guard let image = CIImage(contentsOf: input) else { print("cannot open input"); exit(1) }
let handler = VNImageRequestHandler(ciImage: image)
let request = VNGenerateForegroundInstanceMaskRequest()
try handler.perform([request])
guard let result = request.results?.first else { print("no subject found"); exit(1) }
let buffer = try result.generateMaskedImage(ofInstances: result.allInstances, from: handler, croppedToInstancesExtent: false)
let lifted = CIImage(cvPixelBuffer: buffer)
try CIContext().writePNGRepresentation(of: lifted, to: output, format: .RGBA8, colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!)
print("instances: \(result.allInstances.count), size: \(Int(lifted.extent.width))x\(Int(lifted.extent.height))")
