-- Server-side per-player cooldown. Create one limiter per action.
local RateLimiter = {}
RateLimiter.__index = RateLimiter

function RateLimiter.new(cooldown: number)
    assert(cooldown > 0 and cooldown < math.huge, "Invalid cooldown")
    return setmetatable({cooldown = cooldown, last = {}}, RateLimiter)
end

function RateLimiter:allow(userId: number): boolean
    local now = os.clock()
    local previous = self.last[userId]
    if previous ~= nil and now - previous < self.cooldown then
        return false
    end
    self.last[userId] = now
    return true
end

function RateLimiter:remove(userId: number)
    self.last[userId] = nil
end

return RateLimiter
